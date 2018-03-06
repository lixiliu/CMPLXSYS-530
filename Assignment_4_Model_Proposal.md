# Model Proposal for _Smart Lighting for Offices_

_Lixi Liu_

* Course ID: CMPLXSYS 530,
* Course Title: Computer Modeling of Complex Systems
* Term: Winter, 2018

&nbsp; 

### Goal 
*****
 
_With increasing energy efficiency and smart features that can adapt to occupants' perferences and communicate with other appliances, smart lighting can improve the quality of modern life while reducing energy use and carbon footprint. This study explores how smart lighting sensors interact with Heating Ventilation and Air Conditioning (HVAC) control to maximize occupancy comfort and builing energy savings._

&nbsp;  
### Justification
****
_Agent-based modeling is useful for exploring the nexus between smart/connected lighting and occupants’ preference/comfort in that it can reveal how well smart sensors manipulate room conditions to meet occupants' comfort level according to their control. Understanding these governing interactions between occupants, sensors, and the built environment can maximize the value of smart sensor implementation in buildings to reduce energy use and cost while enhancing ergomonic comfort._

&nbsp; 
### Main Micro-level Processes and Macro-level Dynamics of Interest
****

_This study explores how the interactions 1) among smart sensors and between 2) occupants and sensors affect the system-level energy consumption from lighting and HVAC. The primary focus is on how the daylight controller decides the lighting load reduction potential from daylight harvesting against the added cooling needs from the daylight harvest._

&nbsp; 


## Model Outline
****
&nbsp; 
### 1) Environment
_The environment consists of a single office room serving a speficic function (e.g. room with individual work spaces/cubicles, conference room, pantry, restroom). Its layout (e.g. size, window and door locations) will be defined in the setup._

* _Boundary conditions: fixed (enclosed by walls)_
* _Dimensionality: 2D_
* _List of environment-owned variables:_
..._Current states:_
  + _current harvested lux [lux = lumen/sq m] (amount of daylight entering the room through controllable window blinds)_
  + _current lamp lux (from overhead lamps)_
  + _current total lux (total in-door brightness from overhead lamps and harvested daylight)_
  + _current room temperature [deg F]_
..._Previous states: (for updating)_
  + _previous harvested lux_
  + _previous lamp lux_
  + _previous total lux_
  + _previous room temperature [def F]_
  + _Light energy [kWh]_
  + _HVAC energy [kWh]_
* _List of environment-owned methods/procedures:_
  + _update lux (embedded within agent-specific procedures)_
  + _update room temp (based on previous indoor states, outdoor conditions, and sensor inputs)_
  + _calculate energy (after update to indoor states)_


```python
### Pseudocode ###
def initialize_room():
  gridlen = 15 # x[m] includes some space outside of office
  gridwid = 10 # y[m] includes some space outside of office
  RoomX = range(1,13) # x = 12[m] office length
  RoomY = range(1,9) # y = 8[m] office width
  
  #set walls for office
  #set windows
  #set door
  for x in roomX:
    for y in roomY:
      Cur_harv_lux = 0 # blinds closed, no harvest
      Cur_lamp_lux = 0 #
      Cur_total_lux = Cur_harv_lux + Cur_lamp_lux
      Cur_room_temp = 70 # [deg F]
  Pre_harv_lux = Cur_harv_lux
  Pre_lamp_lux = Cur_harv_lux
  Pre_total_lux = Cur_harv_lux
  Pre_room_temp = Cur_room_temp
  
  Light_energy = [0]
  HVAC_energy = [0]
  
def Update_room_temp():
  Cur_room_temp = f(Pre_room_temp,Outdoor_temp,insulation,Sensors['HVAC'][2],AC_load]

def calc_energy():
  Light_energy.append = f(lamp_efficacy,lamp_distribution,Cur_lamp_lux)
  HVAC_energy.append = AC_load*Sensors['HVAC'][2] 
```

&nbsp; 

### 2) Agents
 
 _There are two main types of agents. The first type is **occupants** in the building, each with a specific schedule, preferences, and comfort level._ 
* _List of occupant-owned variables:_
  + _ID_
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
  + _turn lights on_
  + _turn lights off_

2. _**Daylight controllers** control how much sunlight enters the room by adjusting the window blinds._
* _List of daylight sensor-owned variables:_
  + _None_
* _List of daylight sensor-owned methods/procedures:_ 
  + _adjust blinds (% daylight harvested)_

3. _**Dimmers** instaneously adjust the indoor light level based on the daylight sensor input and the desired indoor lumen level. The dimming is embedded within the motion sensor-owned procedures._

4. _**HVAC controller** controls the room temperature based on the daylight sensor input and the desired indoor temperature. In the cooling mode, when the room temperature rises above a thermostat threshold, the ventilation or AC system would kick in to cool the room until the temperature falls below another thermostat threshold, after which point, the room could heat up again with time and the cycle perpectuates until either the thermostat is turned off or the room temperature ceases to fluctuate beyond the thermostat threholds._
* _List of HVAC controller-owned variables:_
  + _AC on (binary)_
* _List of HVAC controller-owned methods/procedures:_
  + _check temp_

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
    Discomfort[i] = 0
  Pre_position = Cur_position
    
  Sensors = {
  'MoS':[0,0] #[Motion-detected,Timer]
  'DLC':[...]
  'Dim':[...]
  'HVAC':[1,8, 0] #[loc-x, loc-y, AC-on]
  }

# Define Agent Procedures
def Movement(Schedule):
Pre_position = Cur_position
  for i in Schedule:
    if time == Schedule[i][0]: # Enter_room
      Cur_position[i][0] += 1
    elif time > Schedule[i][1]: # Exist_room
      # begin head out room
    else: # Random_Walk within fixed boundary
      if Cur_position[i][0] == RoomX[0] or Cur_position[i][0] == RoomX[len(RoomX)-1]...
      Cur_position[i][1] == RoomY[0] or Cur_position[i][1] == RoomX[len(RoomY)-1]:
        # turn around 180 and walk
      elif :
        if randint(0,1) > 0:
          # random_walk

def Check_discomfort(Occupants,Cur_position, Total_lux,Room_temp):
  for i in Occupants:
    for x in RoomX:
      for y in RoomY:
        if Cur_position[i][0] == x and Cur_position[i][1] == y:
          Discomfort[i].append = 0.5*abs(Total_lux-Occupants[i][0])/Occupants[i][0]...
          +0.5*(Room_temp-Occupants[i][1])/Occupants[i][1]

def Check_motion(Pre_position,Sensors):
  for i in Cur_Position:
    if Cur_position Cur_position[0]-Prev_position[0] > 0 or Cur_position[1]-Prev_position[1] > 0:
      Motion_detected = 1
  if Motion_detected > 0 and Timer < 600:
    Timer += 1
    Adjust_blinds
    Turn_lights_on
  else:
    Turn_lights_off
    
def Adjust_blinds(RoomX,RoomY,Pre_total_lux,Desired_lux,Outdoor_lux):
  for x in RoomX:
    for y in RoomY:
      Cur_harv_lux = min(max(Desired_lux - Pre_total_lux,0),Outdoor_lux)    
      
def Turn_lights_on(RoomX,RoomY,Cur_harv_lux,Desired_lux,Max_lamp_lux): # includes dimming
  for x in RoomX:
    for y in RoomY:
      Cur_lamp_lux = min(max(Desired_lux - Cur_harv_lux,0),Max_lamp_lux)
      Cur_total_lux = Cur_harv_lux + Cur_lamp_lux

def Turn_lights_off(RoomX,RoomY,Cur_harv_lux):
  for x in RoomX:
    for y in RoomY:
      Cur_lamp_lux = 0
      Cur_total_lux = Cur_harv_lux + Cur_lamp_lux

def Check_temp(Sensors,Pre_room_temp):
  Therm_x = Sensors['HVAC'][0]
  Therm_y = Sensors['HVAC'][1]
  if Pre_room_temp(Therm_x,Therm_y) > Desired_temp:
    AC-on = 1
```

&nbsp; 

### 3) Action and Interaction 
 
**_Interaction Topology_**

_The interactions within the systems are predominantly sensor-sensor and sensor-environment, although one occupant-sensor interaction exists. The sensor-sensor communications are network-linked and instantaneous. Updating the state of each patch requires information from the sensors. For the temperature state, it may also require information from neighborhood patches to model convection. The interaction between the occupants and the motion sensor is spatial and temporal (currently, it is assumed that the motion sensing range is of the entire room)._
 
**_Action Sequence_**

_What does an agent, cell, etc. do on a given turn? Provide a step-by-step description of what happens on a given turn for each part of your model_

1. _Occupants move/stay put according to rules and their schedule._
2. _Motion sensor checks for motion and enables other sensors if motion is detected._
3. _Daylight controller adjusts blinds._
4. _Dimmer adjusts light output from lamp._
5. _HVAC controller checks for room temperature and decides whether to turn on AC._
6. _Environment calculates light and HVAC energy use._
7. _Environment updates indoor luminous level and room temperature._

&nbsp; 
### 4) Model Parameters and Initialization

_Global parameters include:_
* _time (time step) - [sec]_
* _outdoor lux - hourly solar insolation relative to time (based on external sources)._
* _outdoor temp - [deg F] hourly temperature relative to time (will be used to determine HVAC load)_
* _desired lux - desired indoor luminous level = average of all occupants' brightness preferences._
* _desired temp - [deg F] desired indoor temperature = average of all occupants' thermal preferences._

_Agent-specific parameters include:_
* _max lamp lux - [lux] maximum lumen output of overhead lamps._
* _lamp_efficacy - [lm/W] amount of lumen output per W of power consumed._
* _thermostat location (shown in Sensors dictionary)_
* _AC load_
* _building insulation_

_To initialize model, set time = 0 and run **initialize_room** and **initialize_agents** from code._

_The step function of the model will consist of advancing the time step by 1 and the **action sequence** described in Section 3._

&nbsp; 

### 5) Assessment and Outcome Measures

_The quantitative metrics of interest in the model are:_
* _Total energy use for light and HVAC_
* _Occupants' comfort level_

&nbsp; 

### 6) Parameter Sweep

_The parameters intended to be swept through are as follows along with their respective value ranges:_
* _occupants' random brightness preference [lux]: [500,1000], which affects the desired lux_
* _occupants' random temperature preference [deg F]: [65,75], which affects the desired temp_

_Besides parameter sweep, different control strategies (e.g. how the sensors update and how their updates are sequenced) may be explored to better understand the interactions between sensors._
