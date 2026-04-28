"""
MQTT Client for EcoPulse
Handles communication with IoT devices (ESP32)
"""

import paho.mqtt.client as mqtt
import logging
from typing import Callable

logger = logging.getLogger(__name__)


class EcoPulseMQTTClient:
    """MQTT client for IoT device communication"""
    
    def __init__(self, broker_host: str = 'localhost', broker_port: int = 1883):
        """
        Initialize MQTT client
        
        Args:
            broker_host: MQTT broker hostname
            broker_port: MQTT broker port
        """
        self.broker_host = broker_host
        self.broker_port = broker_port
        self.client = mqtt.Client()
        self.connected = False
        
    def connect(self) -> bool:
        """Connect to MQTT broker"""
        try:
            self.client.on_connect = self._on_connect
            self.client.on_message = self._on_message
            self.client.connect(self.broker_host, self.broker_port, keepalive=60)
            self.client.loop_start()
            self.connected = True
            logger.info(f"Connected to MQTT broker at {self.broker_host}:{self.broker_port}")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to MQTT broker: {e}")
            return False
    
    def disconnect(self):
        """Disconnect from MQTT broker"""
        self.client.loop_stop()
        self.client.disconnect()
        self.connected = False
        
    def subscribe(self, topic: str):
        """Subscribe to MQTT topic"""
        if self.connected:
            self.client.subscribe(topic)
            logger.info(f"Subscribed to topic: {topic}")
    
    def publish(self, topic: str, payload: str):
        """Publish message to MQTT topic"""
        if self.connected:
            self.client.publish(topic, payload)
            logger.info(f"Published to {topic}: {payload}")
    
    def _on_connect(self, client, userdata, flags, rc):
        """Callback for when client connects"""
        if rc == 0:
            logger.info("MQTT client connected successfully")
        else:
            logger.error(f"MQTT connection failed with code {rc}")
    
    def _on_message(self, client, userdata, msg):
        """Callback for when message is received"""
        logger.info(f"Received message from {msg.topic}: {msg.payload.decode()}")
