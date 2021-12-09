# Project 4
#### by Kenny Nguyen 

## Project Summary

This web application is a place for users to let their imagination and passion for PCs run wild. This web application will allow users to virtually build their own custom PCs from a large database of PC components. User's can then have their virtually customized PCs saved for future reference or even post them publicly for others to view. 

## List of Technologies 
1. Python
2. Masonite
3. Postgres
4. React
5. JavaScript

## Models

List here any models in your app and their properties 
Models I will have in my app are:

### PC Model
| Schema | Description |
|-----|-----|
| Name | Personalized name given from user | 
| Case   | Computer cases from standard sizing to ITX |
| Motherboard | Sizes vary from EATX, ATX, MATX, and ITX |
| Cooler | Can choose between liquid cooling AIOs or air cooling |
| CPU | Intel and AMD options |
| RAM | Dependent on motherboard allowance, users can have 2 or 4 RAM sticks|
| GPU | Choice between recent nVidia RTX 30 series and AMD RX 6000 series cards |
| PSU | Choice between ATX, SFX-L, or SFX |
| Misc | Additional items such as fans or RGB lighting |


### Case Model
| Schema | Description |
| ---- | ---- |
| type | Full, Mid, SFF (Small Form Factor) |
| name | PC Case Name |
| price | price |
| img | Image |

### Motherboard Model 
| Schema | Description |
| ---- | ---- |
| type | EATX, ATX, MATX, ITX |
| name | Motherboard Name |
| ramSlots | How many ram slots the motherboard has |
| price | price |
| img | Image |

### Cooler 
| Schema | Description |
| ---- | ---- |
| Type | AIO or Air |
| Name | Cooler Name |
| price | price |
| img | Image |

### CPU
| Schema | Description |
| ---- | ---- |
| name | CPU Name (brand and series name/number) |
| price | price |
| img | image |

### RAM 
| Schema | Description |
| ---- | ---- |
| name | RAM Name (brand and series name/number) |
| size | Memory size |
| speed | Speed in MHz |
| price | price |
| img | image |

### GPU
| Schema | Description |
| ---- | ---- |
| name | GPU Name (brand and series name/number) |
| price | price |
| img | image |

### PSU 
| Schema | Description |
| ---- | ---- |
| name | PSU Name (brand and series name/number) |
| watts | PSU wattage |
| price | price |
| img | image |

### Misc
| Schema | Description |
| ---- | ---- |
| name | name |
| img | image |

## Route Table

### PC Routes
| url | method | action |
|-----|--------|--------|
| /pc | get | get all pcs |
| /pc/:id | get | get particular |
| /pc | post | create |
| /pc/:id | put | update | 
| /pc/:id | delete | delete | 

### Parts Routes (API)
| url | method | action |
|-----|--------|--------|
| /pc/case| get | get all |
| /pc/case/:id | get | get particular |
| /pc/motherboard| get | get all |
| /pc/motherboard/:id | get | get particular |
| /pc/cooler| get | get all |
| /pc/cooler/:id | get | get particular |
| /pc/cpu| get | get all |
| /pc/cpu/:id | get | get particular |
| /pc/ram| get | get all |
| /pc/ram/:id | get | get particular |
| /pc/gpu| get | get all |
| /pc/gpu/:id | get | get particular |
| /pc/psu| get | get all |
| /pc/psu/:id | get | get particular |
| /pc/misc| get | get all |
| /pc/misc/:id | get | get particular |

### User Stories

- User can create a new pc
- User can pick from a list of items for each component
- User can see full price of the PC they build 
- User can save and/or post their pc
- User can view their pcs
- User can update their own pcs
- User can delete their pcs

### Challenges
- Figuring out how to make the child tables (components) work with the parent table (pc)