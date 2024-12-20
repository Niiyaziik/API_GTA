from fastapi import FastAPI, Query
from typing import List, Optional

app = FastAPI()

data = [
  {
    "id": "1",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/c/c6/Asea2-GTAV-FrontQuarter.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/5/5d/Asea2-GTAV-RearQuarter.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/6/6b/Asea2-GTAV-Front.png/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/8/83/Asea2-GTAV-Rear.png/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/c/ca/Asea2-GTAV-Side.png/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "declasse",
    "model": "asea2"
  },
  {
    "id": "2",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/e/e4/Asea-GTAV-FrontQuarter.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/5/5e/Asea-GTAV-RearQuarter.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/b/b0/Asea-GTAV-Front.png/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/0/0b/Asea-GTAV-Rear.png/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/e/e0/Asea-GTAV-Side.png/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "declasse",
    "model": "asea",
    "seats": 4,
    "price": 12000,
    "topSpeed": {
      "mph": 104,
      "kmh": 167
    },
    "speed": 77.8,
    "acceleration": 50,
    "braking": 13.33,
    "handling": 62.12
  },
  { 
    "id": "3",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/4/43/Asterope-GTAV-FrontQuarter.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/e/ef/Asterope-GTAV-RearQuarter.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/7/79/Asterope-GTAV-Front.png/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/3/32/Asterope-GTAV-Rear.png/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/8/8e/Asterope-GTAV-Side.png/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "karin",
    "model": "asterope",
    "seats": 4,
    "price": 26000,
    "topSpeed": {
      "mph": 105,
      "kmh": 168
    },
    "speed": 77.8,
    "acceleration": 50,
    "braking": 30,
    "handling": 75.76
  },
  { 
    "id": "4",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/b/b9/CogArmored-GTAO-FrontQuarter.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/8/8b/CogArmored-GTAO-RearQuarter.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/7/78/CogArmored-GTAO-Front.png/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/9/98/CogArmored-GTAO-Rear.png/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/2/28/CogArmored-GTAO-Side.png/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "enus",
    "model": "cognoscenti2",
    "seats": 4,
    "price": 558000,
    "topSpeed": {
      "mph": 109,
      "kmh": 175
    },
    "speed": 75.12,
    "acceleration": 63.75,
    "braking": 17.33,
    "handling": 63.64
  },
  {   
    "id": "5",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/3/3f/Cognoscenti55Armored-GTAO-FrontQuarter.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/5/5b/Cognoscenti55Armored-GTAO-RearQuarter.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/7/7b/Cognoscenti55Armored-GTAO-Front.png/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/5/52/Cognoscenti55Armored-GTAO-Rear.png/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/5/56/Cognoscenti55Armored-GTAO-Side.png/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "enus",
    "model": "cog552",
    "seats": 4,
    "price": 396000,
    "topSpeed": {
      "mph": 112,
      "kmh": 180
    },
    "speed": 77.8,
    "acceleration": 65,
    "braking": 18.33,
    "handling": 66.67
  },
  {     
    "id": "6",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/e/ed/Cognoscenti55-GTAO-FrontQuarter.jpg/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/d/d5/Cognoscenti55-GTAO-RearQuarter.jpg/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/8/8c/Cognoscenti55-GTAO-Front.jpg/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/b/bc/Cognoscenti55-GTAO-Rear.jpg/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/6/68/Cognoscenti55-GTAO-Side.jpg/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "enus",
    "model": "cog55",
    "seats": 4,
    "price": 154000,
    "topSpeed": {
      "mph": 112,
      "kmh": 180
    },
    "speed": 77.8,
    "acceleration": 66.25,
    "braking": 19,
    "handling": 66.25
  },
  {     
    "id": "7",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/4/45/Cognoscenti-GTAO-FrontQuarter.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/a/aa/Cognoscenti-GTAO-RearQuarter.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/9/9d/Cognoscenti-GTAO-Front.png/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/9/9d/Cognoscenti-GTAO-Rear.png/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/8/88/Cognoscenti-GTAO-Side.png/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "enus",
    "model": "cognoscenti",
    "seats": 4,
    "price": 254000,
    "topSpeed": {
      "mph": 110,
      "kmh": 176
    },
    "speed": 75.12,
    "acceleration": 65,
    "braking": 18.33,
    "handling": 63.64
  },
  { 
    "id": "8",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/4/4f/EmperorBeater-GTAV-FrontQuarter.jpg/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/b/bc/EmperorBeater-GTAV-RearQuarter.jpg/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/7/78/EmperorBeater-GTAV-Front.jpg/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/8/88/EmperorBeater-GTAV-Rear.jpg/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/a/af/EmperorBeater-GTAV-Side.jpg/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "albany",
    "model": "emperor2",
    "seats": 4,
    "topSpeed": {
      "mph": 90,
      "kmh": 144
    },
    "speed": 64.39,
    "acceleration": 35,
    "braking": 20,
    "handling": 57.58
  },
  { 
    "id": "9",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/c/ce/Emperor3-GTAV-FrontQuarter.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/1/1b/Emperor3-GTAV-RearQuarter.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/e/e3/Emperor3-GTAV-Front.png/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/4/45/Emperor3-GTAV-Rear.png/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/e/e4/Emperor3-GTAV-Side.png/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "albany",
    "model": "emperor3",
    "seats": 4,
    "topSpeed": {
      "mph": 90,
      "kmh": 144
    },
    "speed": 64.39,
    "acceleration": 35,
    "braking": 20,
    "handling": 57.58
  },
  { 
    "id": "10",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/c/c6/EmperorClean-GTAV-FrontQuarter.jpg/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/9/9f/EmperorClean-GTAV-RearQuarter.jpg/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/5/55/EmperorClean-GTAV-Front.jpg/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/a/a1/EmperorClean-GTAV-Rear.jpg/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/5/5e/EmperorClean-GTAV-Side.jpg/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "albany",
    "model": "emperor",
    "seats": 4,
    "topSpeed": {
      "mph": 90,
      "kmh": 144
    },
    "speed": 64.39,
    "acceleration": 35,
    "braking": 20,
    "handling": 57.58
  },
  { 
    "id": "11",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/9/9e/Fugitive-GTAV-FrontQuarter.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/3/3d/Fugitive-GTAV-RearQuarter.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/0/01/Fugitive-GTAV-Front.png/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/f/f4/Fugitive-GTAV-Rear.png/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/9/9e/Fugitive-GTAV-Side.png/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "cheval",
    "model": "fugitive",
    "seats": 4,
    "price": 24000,
    "topSpeed": {
      "mph": 107,
      "kmh": 172
    },
    "speed": 77.8,
    "acceleration": 50,
    "braking": 30,
    "handling": 75.76
  },
  { 
    "id": "12",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/9/96/Glendale-GTAV-FrontQuarter.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/5/51/Glendale-GTAV-RearQuarter.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/1/1f/Glendale-GTAV-Front.png/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/7/76/Glendale-GTAV-Rear.png/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/c/c7/Glendale-GTAV-Side.png/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "benefactor",
    "model": "glendale",
    "seats": 4,
    "price": 200000,
    "topSpeed": {
      "mph": 107,
      "kmh": 172
    },
    "speed": 78.87,
    "acceleration": 58.75,
    "braking": 21.67,
    "handling": 62.12
  },
  { 
    "id": "13",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/a/a5/Ingot-GTAV-FrontQuarter.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/7/76/Ingot-GTAV-RearQuarter.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/f/f2/Ingot-GTAV-Front.png/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/e/e2/Ingot-GTAV-Rear.png/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/2/2e/Ingot-GTAV-Side.png/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "vulcar",
    "model": "ingot",
    "seats": 4,
    "price": 9000,
    "topSpeed": {
      "mph": 90,
      "kmh": 144
    },
    "speed": 67.07,
    "acceleration": 35,
    "braking": 20,
    "handling": 59.09
  },
  { 
    "id": "14",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/0/03/Intruder-GTAV-FrontQuarter.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/f/f0/Intruder-GTAV-RearQuarter.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/d/d2/Intruder-GTAV-Front.png/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/9/95/Intruder-GTAV-Rear.png/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/b/b7/Intruder-GTAV-Side.png/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "karin",
    "model": "intruder",
    "seats": 4,
    "price": 16000,
    "topSpeed": {
      "mph": 106,
      "kmh": 170
    },
    "speed": 77.8,
    "acceleration": 50,
    "braking": 30,
    "handling": 71.21
  },
  { 
    "id": "15",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/0/00/Premier-GTAV-FrontQuarter.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/8/87/Premier-GTAV-RearQuarter.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/6/61/Premier-GTAV-Front.png/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/f/f8/Premier-GTAV-Rear.png/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/a/af/Premier-GTAV-Side.png/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "declasse",
    "model": "premier",
    "seats": 4,
    "price": 10000,
    "topSpeed": {
      "mph": 104,
      "kmh": 167
    },
    "speed": 77.8,
    "acceleration": 50,
    "braking": 20,
    "handling": 63.64
  },
  { 
    "id": "16",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/6/68/PrimoCustom-GTAO-FrontQuarter.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/3/3a/PrimoCustom-GTAO-RearQuarter.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/b/b3/PrimoCustom-GTAO-Front.png/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/e/eb/PrimoCustom-GTAO-Rear.png/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/d/d2/PrimoCustom-GTAO-Side.png/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "albany",
    "model": "primo2",
    "seats": 4,
    "price": 400000,
    "topSpeed": {
      "mph": 103,
      "kmh": 165
    },
    "speed": 75.12,
    "acceleration": 50,
    "braking": 30,
    "handling": 71.21
  },
  { 
    "id": "17",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/4/49/Primo-GTAV-FrontQuarter.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/8/8b/Primo-GTAV-RearQuarter.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/5/53/Primo-GTAV-Front.png/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/a/af/Primo-GTAV-Rear.png/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/e/e8/Primo-GTAV-Side.png/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "albany",
    "model": "primo",
    "seats": 4,
    "price": 9000,
    "topSpeed": {
      "mph": 103,
      "kmh": 165
    },
    "speed": 75.12,
    "acceleration": 50,
    "braking": 30,
    "handling": 71.21
  },
  { 
    "id": "18",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/c/ce/Regina-GTAV-FrontQuarter.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/7/7e/Regina-GTAV-RearQuarter.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/4/4f/Regina-GTAV-Front.png/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/1/10/Regina-GTAV-Rear.png/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/8/8e/Regina-GTAV-Side.png/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "dundreary",
    "model": "regina",
    "seats": 4,
    "price": 8000,
    "topSpeed": {
      "mph": 86,
      "kmh": 138
    },
    "speed": 64.39,
    "acceleration": 35,
    "braking": 20,
    "handling": 57.58
  },
  { 
    "id": "19",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/e/ef/RomeroHearse-GTAV-FrontQuarter.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/e/e5/RomeroHearse-GTAV-RearQuarter.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/c/ce/RomeroHearse-GTAV-Front.png/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/d/d3/RomeroHearse-GTAV-Rear.png/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/8/85/RomeroHearse-GTAV-Side.png/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "albany",
    "model": "romero",
    "seats": 4,
    "price": 45000,
    "topSpeed": {
      "mph": 89,
      "kmh": 143
    },
    "speed": 67.07,
    "acceleration": 37.5,
    "braking": 16.67,
    "handling": 59.09
  },
  { 
    "id": "20",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/5/5d/SchafterLWBArmored-GTAO-FrontQuarter.jpg/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/1/18/SchafterLWBArmored-GTAO-RearQuarter.jpg/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/e/e3/SchafterLWBArmored-GTAO-Front.jpg/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/5/5e/SchafterLWBArmored-GTAO-Rear.jpg/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/e/e6/SchafterLWBArmored-GTAO-Side.jpg/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "benefactor",
    "model": "schafter6",
    "seats": 4,
    "price": 438000,
    "topSpeed": {
      "mph": 109,
      "kmh": 175
    },
    "speed": 76.19,
    "acceleration": 46.25,
    "braking": 27.33,
    "handling": 77.27
  },
  { 
    "id": "21",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/7/7c/SchafterV12Armored-GTAO-front.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/7/7d/SchafterV12Armored-GTAO-rear.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/9/9b/SchafterV12Armored-GTAO-Front.jpg/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/d/d7/SchafterV12Armored-GTAO-Rear.jpg/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/e/e2/SchafterV12Armored-GTAO-Side.jpg/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "benefactor",
    "model": "schafter5",
    "seats": 4,
    "price": 325000,
    "topSpeed": {
      "mph": 123,
      "kmh": 197
    },
    "speed": 80.48,
    "acceleration": 72.5,
    "braking": 30.67,
    "handling": 77.27
  },
  { 
    "id": "22",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/2/2a/Schafter-GTAV-FrontQuarter.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/2/24/Schafter-GTAV-RearQuarter.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/1/1b/Schafter-GTAV-Front.png/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/1/17/Schafter-GTAV-Rear.png/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/2/2e/Schafter-GTAV-Side.png/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "benefactor",
    "model": "schafter2",
    "seats": 4,
    "price": 65000,
    "topSpeed": {
      "mph": 110,
      "kmh": 176
    },
    "speed": 77.8,
    "acceleration": 50,
    "braking": 30,
    "handling": 77.27
  },
  { 
    "id": "23",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/9/93/Stafford-GTAO-FrontQuarter.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/3/36/Stafford-GTAO-RearQuarter.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/c/c8/Stafford-GTAO-Front.png/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/b/be/Stafford-GTAO-Rear.png/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/8/82/Stafford-GTAO-Side.png/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "enus",
    "model": "stafford",
    "seats": 4,
    "price": 1272000,
    "topSpeed": {
      "mph": 93,
      "kmh": 149
    },
    "speed": 64.39,
    "acceleration": 50,
    "braking": 15,
    "handling": 60.61
  },
  { 
    "id": "24",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/3/3a/Stanier-GTAV-FrontQuarter.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/c/cc/Stanier-GTAV-RearQuarter.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/c/c9/Stanier-GTAV-Front.jpg/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/2/2a/Stanier-GTAV-Rear.jpg/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/4/4f/Stanier-GTAV-Side.jpg/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "vapid",
    "model": "stanier",
    "seats": 4,
    "price": 10000,
    "topSpeed": {
      "mph": 108,
      "kmh": 173
    },
    "speed": 75.12,
    "acceleration": 50,
    "braking": 30,
    "handling": 74.24
  },
  { 
    "id": "25",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/d/d4/Stratum-GTAV-frontquarter.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/3/3e/Stratum-GTAV-rearquarter.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/4/43/Stratum-GTAV-Front.png/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/2/22/Stratum-GTAV-Rear.png/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/d/dd/Stratum-GTAV-side.png/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "zirconium",
    "model": "stratum",
    "seats": 4,
    "price": 10000,
    "topSpeed": {
      "mph": 104,
      "kmh": 167
    },
    "speed": 72.43,
    "acceleration": 52.5,
    "braking": 20,
    "handling": 66.67
  },
  { 
    "id": "26",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/d/d0/Stretch-GTAV-FrontQuarter.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/7/72/Stretch-GTAV-RearQuarter.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/f/f7/Stretch-GTAV-Front.png/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/5/5a/Stretch-GTAV-Rear.png/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/4/40/Stretch-GTAV-Side.png/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "dundreary",
    "model": "stretch",
    "seats": 6,
    "price": 30000,
    "topSpeed": {
      "mph": 94,
      "kmh": 151
    },
    "speed": 72.43,
    "acceleration": 42.5,
    "braking": 26.67,
    "handling": 56.06
  },
  { 
    "id": "27",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/2/2b/SuperDiamond-GTAV-FrontQuarter.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/b/ba/SuperDiamond-GTAV-RearQuarter.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/a/a3/SuperDiamond-GTAV-Front.png/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/a/ac/SuperDiamond-GTAV-Rear.png/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/7/78/SuperDiamond-GTAV-Side.png/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "enus",
    "model": "superd",
    "seats": 4,
    "price": 250000,
    "topSpeed": {
      "mph": 111,
      "kmh": 178
    },
    "speed": 77.8,
    "acceleration": 65,
    "braking": 20,
    "handling": 63.64
  },
  { 
    "id": "28",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/5/53/Surge-GTAV-FrontQuarter.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/b/b0/Surge-GTAV-RearQuarter.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/6/6d/Surge-GTAV-FrontView.png/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/4/4e/Surge-GTAV-RearView.png/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/6/67/Surge-GTAV-Side.png/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "cheval",
    "model": "surge",
    "seats": 4,
    "price": 38000,
    "topSpeed": {
      "mph": 93,
      "kmh": 149
    },
    "speed": 75.12,
    "acceleration": 25,
    "braking": 20,
    "handling": 65.15
  },
  { 
    "id": "29",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/7/72/Tailgater-GTAV-FrontQuarter.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/f/f0/Tailgater-GTAV-RearQuarter.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/5/59/Tailgater-GTAV-Front.png/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/3/35/Tailgater-GTAV-Rear.png/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/d/df/Tailgater-GTAV-Side.png/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "obey",
    "model": "tailgater",
    "seats": 4,
    "price": 55000,
    "topSpeed": {
      "mph": 104,
      "kmh": 167
    },
    "speed": 77.8,
    "acceleration": 50,
    "braking": 30,
    "handling": 77.27
  },
  {  
    "id": "30",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/3/39/TurretedLimo-GTAO-front.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/9/9b/TurretedLimo-GTAO-rear.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/6/6a/TurretedLimo-GTAO-frontView.png/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/1/13/TurretedLimo-GTAO-rearView.png/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/c/c0/TurretedLimo-GTAO-side.png/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "benefactor",
    "model": "limo2",
    "seats": 6,
    "price": 1650000,
    "topSpeed": {
      "mph": 89,
      "kmh": 143
    },
    "speed": 67.07,
    "acceleration": 67.5,
    "braking": 26.67,
    "handling": 65.91
  },
  { 
    "id": "31",
    "images": {
      "frontQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/2/2e/Warrener-GTAV-FrontQuarter.png/revision/latest/scale-to-width-down/210",
      "rearQuarter": "https://vignette.wikia.nocookie.net/gtawiki/images/3/36/Warrener-GTAV-RearQuarter.png/revision/latest/scale-to-width-down/210",
      "front": "https://vignette.wikia.nocookie.net/gtawiki/images/c/ce/Warrener-GTAV-Front.png/revision/latest/scale-to-width-down/210",
      "rear": "https://vignette.wikia.nocookie.net/gtawiki/images/8/87/Warrener-GTAV-Rear.png/revision/latest/scale-to-width-down/210",
      "side": "https://vignette.wikia.nocookie.net/gtawiki/images/c/c6/Warrener-GTAV-Side.png/revision/latest/scale-to-width-down/210"
    },
    "manufacturer": "vulcar",
    "model": "warrener",
    "seats": 4,
    "price": 120000,
    "topSpeed": {
      "mph": 103,
      "kmh": 165
    },
    "speed": 75.12,
    "acceleration": 61.25,
    "braking": 31.67,
    "handling": 65.45
  }
]

@app.get("/characters/")
async def get_characters(
    model: Optional[str] = Query(None, description="Поиск по имени"),
    page: int = Query(1, ge=1, description="Номер страницы"),
    size: int = Query(10, ge=1, description="Размер страницы")
):
    filtered_data = (
        [item for item in data if model.lower() in item["model"].lower()]
        if model else data
    )

    total_items = len(filtered_data)
    start_index = (page-1) * size
    end_index = page * size
    paginated_data = filtered_data[start_index:end_index]

    total_pages = (total_items + size - 1) // size
    next_page = page + 1 if page <= total_pages else total_pages + 1
    return {"meta": 
      {"pagination": {
          "current": page,
          "next": next_page,
          "last": total_pages
        }
      }, 
      "data": paginated_data
    }

@app.get("/")
def read_root():
    return {"message": "API is working"}