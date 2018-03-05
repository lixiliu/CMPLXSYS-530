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
_The environment consists of a single-floor office with rooms serving different functions (e.g. work spaces, conference rooms, pantry) as well as the amount of daylight entering the rooms through window blinds)._

* _Boundary conditions: fixed (office enclosed by walls)_
* _Dimensionality: 2D_
* _List of environment-owned variables: amount of reflected daylight_
* _List of environment-owned methods/procedures (e.g. resource production, state change, etc.)_


```python
# Include first pass of the code you are thinking of using to construct your environment
# This may be a set of "patches-own" variables and a command in the "setup" procedure, a list, an array, or Class constructor
# Feel free to include any patch methods/procedures you have. Filling in with pseudocode is ok! 
# NOTE: If using Netlogo, remove "python" from the markdown at the top of this section to get a generic code block
```

&nbsp; 

### 2) Agents
 
 _There are two types of agents. The first type is occupants (workers) in the building, with random movement, transition status (when to arrive and leave work, etc), and heterogeneous preference for luminous level. The second type is dimming sensors that adjust the indoor light level based on the daylight feedback and the occupants’ specified preference._
 
* _List of occupant-owned variables:_ 

...* _daily schedule_

* _List of occupant-owned methods/procedures: (e.g. move, consume, reproduce, die, etc.)_


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
* _time - the length of a typical work day discretized into hourly steps._
* _daylight - hourly solar insolation relative to time (obtained from NREL databsed)._

_Describe how your model will be initialized_

_Provide a high level, step-by-step description of your schedule during each "tick" of the model_

&nbsp; 

### 5) Assessment and Outcome Measures

_What quantitative metrics and/or qualitative features will you use to assess your model outcomes?_

&nbsp; 

### 6) Parameter Sweep

_What parameters are you most interested in sweeping through? What value ranges do you expect to look at for your analysis?_

