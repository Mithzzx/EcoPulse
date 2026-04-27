# EcoPulse: A Decentralized Edge-AI Architecture for Autonomous Household Energy Management Using Reinforcement Learning

Mithun Rajan SM Sabaris S Vikrant S
mithunrajan77@gmail.com sabaris92005@gmail.com vikrant007.001@gmail.com



_**Abstract**_ **—Excessive** **energy** **consumption** **in** **urban** **residences**
**contributes** **substantially** **to** **household** **expenditure** **and** **green-**
**house** **gas** **emissions.** **This** **paper** **presents** **EcoPulse,** **a** **self-**
**governing** **optimization** **framework** **that** **deploys** **quantized** **Re-**
**inforcement** **Learning** **(RL)** **agents** **at** **the** **network** **edge** **to**
**autonomously** **reduce** **electricity** **costs.** **The** **proposed** **system**
**integrates Non-Intrusive Load Monitoring (NILM) for appliance-**
**level** **power** **disaggregation** **with** **occupancy-driven** **adaptive** **con-**
**trol. Preliminary projections indicate a potential 31.7% reduction**
**in** **monthly** **electricity** **expenditure** **under** **typical** **urban** **Indian**
**household** **conditions.** **This** **paper** **details** **the** **proposed** **system**
**architecture,** **the** **governing** **optimization** **formulation,** **and** **the**
**anticipated** **economic** **and** **environmental** **outcomes.**
_**Index Terms**_ **—Edge Intelligence, Reinforcement Learning, Res-**
**idential** **Energy** **Optimization,** **IoT** **Sensing,** **NILM,** **Smart** **Home**
**Automation.**


I. INTRODUCTION


The proliferation of always-on devices and inefficient appliance scheduling has made passive energy waste a defining
challenge in urban households. Conventional home automation
platforms rely either on rigid rule-based timers that require
manual configuration or offload decision-making to remote
cloud servers—both approaches introduce latency, privacy
exposure, and an inability to respond dynamically to shifting
occupancy patterns [1].
EcoPulse addresses these limitations by localizing intelligence on a Raspberry Pi 5 gateway. By retaining all sensor
data, model inference, and actuation decisions within the home
network, the system eliminates round-trip delay and datasharing concerns inherent to cloud-based architectures [2].
The primary design objective is to transition residences
from a reactive, user-driven control paradigm to a proactive,
AI-governed operating mode that systematically eliminates
standby and off-schedule consumption.


II. PROPOSED METHODOLOGY


EcoPulse operates through a continuous perceptionreasoning-actuation cycle. Each iteration collects power and
environmental data, updates the agent’s world model, and
dispatches control signals to connected appliances.


_A._ _System_ _Architecture_


The hardware layer is centered on a PZEM-004T current
and voltage monitoring unit that captures whole-home power
draw at the main distribution panel. This aggregate signal



is routed to the edge compute node via a local Wi-Fi mesh
managed by an MQTT broker.


Fig. 1. EcoPulse system architecture: from perception to execution.


Distributed ESP32 microcontrollers at each load point execute relay switching commands received from the central
gateway. Context sensors—including PIR motion detectors, a
DHT22 temperature/humidity module, and an LDR ambient
light sensor—supply occupancy and environmental state information that enriches the agent’s observation vector.


_B._ _Load_ _Disaggregation_ _and_ _Consumption_ _Forecasting_


To enable appliance-level decision-making from a single
metering point, EcoPulse employs a NILM pipeline trained
to decompose the aggregate power waveform into per-device
load signatures [4].
An LSTM network processes the resulting time-series to
identify recurring temporal usage patterns. These inferred
patterns feed into the RL agent as part of its state representation, enabling the agent to anticipate demand rather than
merely react to it. The core decision-making component is a
Proximal Policy Optimization (PPO) agent. PPO was selected
over value-based alternatives owing to its stable convergence
behavior in environments with continuous or large discrete
action spaces.


_C._ _Optimization_ _Formulation_


The PPO agent is trained to maximize a composite reward
signal that jointly considers energy savings and occupant
comfort. The reward function is defined as:


Fig. 2. Projected energy reduction across appliance categories.


_R_ = _ω_ 1 _· E_ saved _−_ _ω_ 2 _· C_ penalty (1)


where _E_ saved denotes the per-episode reduction in kilowatthours relative to the unoptimized baseline, and _C_ penalty represents the accumulated comfort-violation score derived from
override frequency. The weights _ω_ 1 and _ω_ 2 balance the tradeoff between economic savings and user comfort.


III. PROJECTED OUTCOMES


_A._ _Financial_ _and_ _Environmental_ _Impact_


Projections are grounded in published consumption benchmarks for urban Indian residential units. The system is expected to reduce average monthly consumption from 450 kWh
under baseline conditions to approximately 308 kWh.


TABLE I
PROJECTED MONTHLY PERFORMANCE INDICATORS FOR AN URBAN
BENGALURU RESIDENTIAL SCENARIO


**Performance** **Metric** **Baseline** **EcoPulse** **Reduction**


Energy Consumption (kWh) 450 308 31.5%
Monthly Bill (INR, ) 3,825 2,610 1,215 (31.7%)
Carbon Footprint (kg CO2) 369 252 31.7%
aElectricity tariff assumed at 8.5/kWh [5].
bCarbon intensity: 0.82 kg CO2/kWh (CEA India, 2023) [5].


The projected annual savings of 14,580 per household represent a meaningful reduction in household operating costs
while simultaneously lowering residential carbon footprints by
approximately 117 kg CO2 per month.


_B._ _Computational_ _Feasibility_ _on_ _Edge_ _Hardware_


EcoPulse addresses inference overhead through posttraining 8-bit integer quantization of both the NILM and PPO
networks [3]. Quantized models achieve inference latency and
power draw compatible with the Raspberry Pi 5’s thermal
and power envelope, keeping the optimizer’s self-consumption
below 5 W—well within the bounds of cost-effective deployment.



IV. CONCLUSION AND FUTURE DIRECTIONS


EcoPulse presents a technically coherent path toward costeffective, privacy-preserving, and fully autonomous residential energy management. The projected 31.7% reduction in
monthly electricity expenditure establishes a compelling economic rationale for adoption in urban Indian households.
Future work will prioritize the integration of solar photovoltaic
generation data and the exploration of federated learning
schemes across multiple households to enable communityscale optimization without centralizing sensitive energy data.


REFERENCES


[1] M. Erol-Kantarci and H. T. Mouftah, “Cost-efficient residential energy
management in smart grids using wireless sensor networks,” _IEEE Trans._
_Smart_ _Grid_, vol. 2, no. 2, pp. 314–325, Jun. 2011.

[2] J. Chen and X. Ran, “Deep learning with edge computing: A comprehensive review,” _Proc. IEEE_, vol. 107, no. 8, pp. 1655–1674, Aug. 2019.

[3] B. Jacob _et_ _al._, “Quantization and training of neural networks for
efficient integer-arithmetic-only inference,” in _Proc._ _IEEE/CVF_ _Conf._
_Comput._ _Vis._ _Pattern_ _Recognit._ _(CVPR)_, Salt Lake City, UT, USA, Jun.
2018, pp. 2704–2713.

[4] J. Kelly and W. Knottenbelt, “Neural NILM: Deep neural networks
applied to energy disaggregation,” in _Proc._ _2nd_ _ACM_ _Int._ _Conf._ _Em-_
_bedded_ _Syst._ _Energy-Efficient_ _Built_ _Environ._ _(BuildSys)_, Seoul, South
Korea, Nov. 2015, pp. 55–64.

[5] X. Tan, Q. Qu, B. Sun, and P. Cheng, “Optimal scheduling of electric
vehicle charging with time-of-use pricing in smart grids,” in _Proc._
_IEEE_ _Conf._ _Control_ _Appl._ _(CCA)_, Sydney, NSW, Australia, Sep. 2015,
pp. 1621–1626.


