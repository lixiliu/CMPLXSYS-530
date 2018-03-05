# Model Proposal for _Smart Lighting for Offices_

_Lixi Liu_

* Course ID: CMPLXSYS 530,
* Course Title: Computer Modeling of Complex Systems
* Term: Winter, 2018



&nbsp; 

### Goal 
*****
 
_With increasing energy efficiency and smart features that can adapt to occupants' perferences and communicate with other appliances, smart lighting can improve the quality of modern life while reducing energy use and carbon footprint. This study explores whether smart lighting sensors and program can help minimize energy rebound, a common behavioral tendency in which occupants increase consumption post-adoption of more energy-efficient products, thus leading to an erosion of energy savings._

&nbsp;  
### Justification
****
_Agent-based modeling is used to examine system-level behaviors that are emerging from individual agent-agent and agent-environment interactions. It is thus useful for exploring the nexus between smart/connected lighting and occupants’ preference/comfort. An agent-based model can reveal the emergent patterns that arise from how occupants interact with smart sensors and how smart sensors, in turn, affect their lifestyle. Understanding these interactions can enhance the use of energy efficiency and demand response as viable tools for lowering building energy costs and improving the reliability of the power grid._

&nbsp; 
### Main Micro-level Processes and Macro-level Dynamics of Interest
****

_This study explores the interactions between occupants and smart sensors: 1) ._

&nbsp; 


## Model Outline
****
&nbsp; 
### 1) Environment
_The environment consists of a single office room serving a speficic function (e.g. room with individual work spaces/cubicles, conference room, pantry, restroom). Its layout (e.g. size, window and door locations) will be defined in the setup._

* _Boundary conditions: fixed (enclosed by walls)_
* _Dimensionality: 2D_
* _List of environment-owned variables:_
  + _reflected daylight (amount of daylight entering the room through controllable window blinds)_
  + _luminous level (total brightness from overhead lamps and reflected daylight)_
  + _room temperature (assume uniform)_
* _List of environment-owned methods/procedures:_
  + _adjust dimming_
  + _adjust temperature_


```python
# Pseudocode:
def Room():

```

&nbsp; 

### 2) Agents
 
 _There are two main types of agents. The first type is **occupants** (workers) in the building, each with a specific work schedule and preference for luminous level._ 
* _List of occupant-owned variables:_
  + _schedule (e.g. when to enter and leave room)_
  + _brightness preference_
  + _thermal preference_ 
  + _satisfaction level (of room condition relative to preference, equally weighted between brightness and temperature)_
* _List of occupant-owned methods/procedures:_
  + _enter room_
  + _leave room_
  + _move (with some probability of being still, e.g. sitting at a meeting, working at a desk)_

_The second type is **sensors**, which include: motion sensors, daylight sensors, and HVAC sensors._
1. **Motion sensors** turn lights on based on occupants' movement and keep them on for some time after the last detected movement. Motion sensors are best for high-motion, low traffic rooms such as restrooms or pantry.
* _List of motion sensor-owned variables:_
  + _motion-detected? (binary)_
  + _timer (number of time steps since the last detected motion)_
* _List of motion sensor-owned methods/procedures:_
  + _turn on/off_

_The third type adjust the indoor light level based on the daylight feedback and the occupants’ specified preference._
* _List of sensor-owned variables:__
* _List of sensor-owned methods/procedures: adjust_brightness_


```python
# Include first pass of the code you are thinking of using to construct your agents
# This may be a set of "turtle-own" variables and a command in the "setup" procedure, a list, an array, or Class constructor
# Feel free to include any agent methods/procedures you have so far. Filling in with pseudocode is ok! 
# NOTE: If using Netlogo, remove "python" from the markdown at the top of this section to get a generic code block
```

&nbsp; 

### 3) Action and Interaction 
 
**_Interaction Topology_**

_Description of the topology of who interacts with whom in the system. Perfectly mixed? Spatial proximity? Along a network? CA neighborhood?_
 
**_Action Sequence_**

_What does an agent, cell, etc. do on a given turn? Provide a step-by-step description of what happens on a given turn for each part of your model_

1. Step 1
2. Step 2
3. Etc...

&nbsp; 
### 4) Model Parameters and Initialization

_Global parameters include:_
* _time - the length of a typical work day discretized into 5-min intervals._
* _daylight - hourly solar insolation relative to time (obtained from NREL databsed)._

_Describe how your model will be initialized_

_Provide a high level, step-by-step description of your schedule during each "tick" of the model_

&nbsp; 

### 5) Assessment and Outcome Measures

_What quantitative metrics and/or qualitative features will you use to assess your model outcomes?_

&nbsp; 

### 6) Parameter Sweep

_What parameters are you most interested in sweeping through? What value ranges do you expect to look at for your analysis?_

