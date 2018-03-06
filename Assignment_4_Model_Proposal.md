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
  + _current harvested lux [lux = lumen/sq m] (amount of daylight entering the room through controllable window blinds)_
  + _previous harvested lux [lux]
  + _current lamp lux [lux] (from overhead lamps)_
  + _previous lamp lux [lux]
  + _current total lux [lux] (total in-door brightness from overhead lamps and harvested daylight)_
  + _previous total lux [lux]
  + _current room temperature [deg F] (assume spatially uniform)_
  + _previous room temperature [def F]_
* _List of environment-owned methods/procedures:_
  + _update lux (based on previous indoor state, outdoor conditions, and sensor inputs)_
  + _update room temp (based on previous indoor state, outdoor conditions, and sensor inputs)_


```python
### Pseudocode ###
def initialize_room():
  gridlen = 15 # x[m] includes some space outside of office
  gridwid = 10 # y[m] includes some space outside of office
  roomX = range(1,13) # x = 12[m] office length
  roomY = range(1,9) # y = 8[m] office width
  
  #set walls for office
  #set windows
  #set door
  for x in roomX:
    for y in roomY:
      Cur_harv_lux = 0 # blinds closed, no harvest
      Cur_lamp_lux = 750 #
      Cur_total_lux = Harvested_lux
      Cur_room_temp = 70 # [deg F]
  Pre_harv_lux = Cur_harv_lux
  Pre_lamp_lux = Cur_harv_lux
  Pre_total_lux = Cur_harv_lux
  Pre_room_temp = Cur_room_temp
  
def Update_lux():

def Update_room_temp():
```

&nbsp; 

### 2) Agents
 
 _There are two main types of agents. The first type is **occupants** in the building, each with a specific schedule, preferences, and comfort level._ 
* _List of occupant-owned variables:_
  + _ID
  + _schedule (e.g. when to enter and leave room)_
  + _brightness preference_
  + _thermal preference_ 
  + _discomfort level (preference satisfaction, equally weighted between brightness and temperature)_
  + _current position_
  + _previous position_
* _List of occupant-owned methods/procedures:_
  + _enter room_
  + _exit room_
  + _move (with some probability of being still, e.g. sitting at a meeting, working at a desk)_
  + _check discomfort_

_The second type of agents is **sensors**, which include: motion sensors, daylight controllers, dimmers and HVAC controller._
1. _**Motion sensors** turn lights on based on occupants' movement and keep them on for some time after the last detected movement. Motion sensors are best for high-motion, low traffic rooms such as restrooms or pantry._
* _List of motion sensor-owned variables:_
  + _motion detected (binary)_
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
### Psudocode ###
from random import randint
# Define Agent Variables
def Initialize_agents():
  Population = 4
  Occupants = {}
  Schedule = {}
  Cur_position = {}
  Discomfort = {}
  For i in range(Population):
    Occupants[i] = [randint(500,1200),randint(60,78)] # [brightness pref(lux), thermal pref(deg F)]
    Schedule[i] = [randint(0,10), randint(300,1200)] # [enter time, time to begin leaving room]
    Cur_Position[i] = [0,5,90] # [x,y,orientation] (e.g. at entrance of door)
  Pre_position = Cur_position
    
  Sensors = {
  'MoS':[0,0] #[Motion-detected,Timer]
  'DLC':[...]
  'Dim':[...]
  'HVAC':[...]
  }

# Define Agent Procedures
def Movement(Schedule):
Pre_Position = Cur_Position
  for i in Schedule:
    if time == Schedule[i][0]: # Enter_room
      Cur_Position[i][0] += 1
    elif time > Schedule[i][1]: # Exist_room
      # begin head out room
    else: # Random_Walk
      if Cur_Position[i][0] == x-boundary or Cur_Position[i][1] == y-boundary:
        # turn around and walk
      else:
        if randint(0,1) > 0:
          # random_walk

def Check_discomfort(Occupants,Cur_position, Total_lux,Room_temp):
  for i in Occupants:
    for x in RoomX:
      for y in RoomY:
        if Cur_position[i][0] == x and Cur_position[i][1] == y:
          Discomfort[i].append = 0.5*abs(Total_lux-Occupants[i][0])+0.5*(Room_temp-Occupants[i][1])

def Check_motion(Cur_position, Pre_position, Sensors):
  for i in Cur_Position:
    if Cur_position[0]-Prev_position[0] > 0 or Cur_position[1]-Prev_position[1] > 0:
      Motion_detected = 1
      Turn_lights_on
  if Motion_detected > 0 and Timer < 600:
    Timer += 1
  else:
    Turn_lights_off
    
def Turn_lights_on(Sensors):
  

def Turn_lights_off(Sensors):

def Adjust_blinds():
  if 

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
* _time - [sec]_
* _outdoor daylight - [lux] hourly solar insolation relative to time (based on external sources)._
* _outdoor temperature - [deg F] hourly relative to time (will be used to determine HVAC load)_
* _desired indoor lumen level [lux] (average of all occupants' preferences)._
* _desired indoor temperature [deg F] (average of all occupants' preferences)._

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

_The parameters intended to be swept through are as follows along with their respective value ranges:_
* _desired indoor lumen level: []_
* _desired indoor temperature: [65,75]_
