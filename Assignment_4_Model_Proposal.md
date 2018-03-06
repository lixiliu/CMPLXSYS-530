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
  + _harvested daylight (amount of daylight entering the room through controllable window blinds)_
  + _light level (from overhead lamps)_
  + _total lumen level (total in-door brightness from overhead lamps and harvested daylight)_
  + _room temperature (assume uniform and steady-state)_
* _List of environment-owned methods/procedures:_
  + _update luminous level (based on current indoor state, outdoor conditions, and sensor inputs)_
  + _update room temperture (based on current indoor state, outdoor conditions, and sensor inputs)_


```python
# Pseudocode:
# def Room():

```

&nbsp; 

### 2) Agents
 
 _There are two main types of agents. The first type is **occupants** in the building, each with a specific schedule, preferences, and comfort level._ 
* _List of occupant-owned variables:_
  + _ID
  + _schedule (e.g. when to enter and leave room)_
  + _brightness preference_
  + _thermal preference_ 
  + _comfort level (preference satisfaction, equally weighted between brightness and temperature)_
  + _previous position_
  + _current position_
* _List of occupant-owned methods/procedures:_
  + _enter room_
  + _leave room_
  + _move (with some probability of being still, e.g. sitting at a meeting, working at a desk)_

_The second type of agents is **sensors**, which include: motion sensors, daylight controllers, dimmers and HVAC controller._
1. _**Motion sensors** turn lights on based on occupants' movement and keep them on for some time after the last detected movement. Motion sensors are best for high-motion, low traffic rooms such as restrooms or pantry._
* _List of motion sensor-owned variables:_
  + _motion detected? (binary)_
  + _timer (number of time steps since the last detected motion)_
* _List of motion sensor-owned methods/procedures:_
  + _check motion_
  + _turn lights on/off_

2. _**Daylight controllers** control how much sunlight enters the room by adjusting the window blinds._
* _List of daylight sensor-owned variables:_
  + _None_
* _List of daylight sensor-owned methods/procedures:_ 
  + _adjust blinds (% daylight harvested)_

3. _**Dimmers** instaneously adjust the indoor light level based on the daylight sensor input and the desired indoor lumen level._
* _List of dimmer-owned variables:_
  + _None_
* _List of dimmer-owned methods/procedures:_
  + _check and adjust light level_

4. _**HVAC controller** controls the room temperature based on the daylight sensor input the desired indoor temperature._
* _List of HVAC controller-owned variables:_
  + _None_
* _List of HVAC controller-owned methods/procedures:_
  + _check and adjust temperature_

```python
# def Init_agents:
  Occupants = {}
  Schedule = {}
  Cur_Position = {}
  For i in range(10):
    Occupants[i+1] = [rand(50,60),rand(60,78),0] # [brightness pref, thermal pref, comfort level]
    Schedule[i+1] = [rand(0,10), rand(300,1200)] # [enter time, leave time]
    Cur_Position[i+1] = [0,0] # (e.g. entrance of door)
  Pre_Position = Cur_Position
    
  Sensors = {
  'MoS':[...]
  'DLC':[...]
  'Dim':[...]
  'HVAC':[...]
  }
    
# def Enter_room(Schedule):
  for i in Schedule:
    if time == 
Occupants
# def Check_motion(Occupants, Sensors):
  if Occupants[Current_Position] - Occupants[Previous_Position] > 0:
    motion_detected? = 1
    turn lights on
  if motion_detected? > 0 and timer < 600:
    timer += 1
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
* _time - time step in seconds._
* _outdoor daylight - hourly solar insolation relative to time (based on external sources)._
* _outdoor temperature - hourly relative to time (will be used to determine HVAC load)_
* _desired indoor lumen level (average of all occupants' preferences)._
* _desired indoor temperature (average of all occupants' preferences)._

_Describe how your model will be initialized_

_Provide a high level, step-by-step description of your schedule during each "tick" of the model_

&nbsp; 

### 5) Assessment and Outcome Measures

_The quantitative metrics of interest in the model are:_
* _Total energy use for light and HVAC_
* _Occupants' comfort level_

_The qualitative features will you use to assess your model outcomes?_

&nbsp; 

### 6) Parameter Sweep

_What parameters are you most interested in sweeping through? What value ranges do you expect to look at for your analysis?_

