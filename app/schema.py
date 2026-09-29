from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Annotated
from enum import Enum


class EquipmentInfo(str, Enum):
    DryVan = "Dry Van"
    Reeferequipment = "Reefer equipment"
    Flatbed = "Flatbed"
    

class Freight_rate_input(BaseModel):

    pickup: Annotated[
        str,
        Field(
            ...,
            min_length=2,
            max_length=50,
            title="Pickup",
            examples=["Oklahoma City"],
            description="Enter your pickup spot between 2-50 characters"
        )
    ]

    delivery: Annotated[
        str,
        Field(
            ...,
            min_length=2,
            max_length=50,
            title="Delivery",
            examples=["Hartford"],
            description="Enter your delivery destination between 2-50 characters"
        )
    ]

    distance: Annotated[
        int,
        Field(
            ...,
            ge=1,
            le=10000,
            title="Distance",
            description="Distance should be between 1 and 10000 miles"
        )      
        
    ]

    equipment: EquipmentInfo

    weight: Annotated[
        int,
        Field(
            ...,
            ge=1,
            le=100000,
            title="Weight",
            examples=[1000],
            description="Weight should be between 1 and 100000 lb"
        )
    ]

    year: Annotated[
        int,
        Field(
            ...,
            ge=2000,
            le=2100,
            title="Year",
            examples=[2025],
            description="Enter the year"
        )
    ]

    month: Annotated[
        int,
        Field(
            ...,
            ge=1,
            le=12,
            title="Month",
            examples=[12],
            description="Enter the month between 1 and 12"
        )
    ]

    day: Annotated[
        int,
        Field(
            ...,
            ge=1,
            le=31,
            title="Day",
            examples=[15],
            description="Enter the day between 1 and 31"
        )
    ]
    
    
    # Filtering Pickup more deeply...
    @field_validator("pickup")
    @classmethod
    def validate_pickup(cls, value: str):
   
        words = value.strip().split()
   
        for word in words:
   
           if not word:
               continue
   
           if not word[0].isupper():
               raise ValueError(
                   "Each word must start with an uppercase letter."
               )
   
           if len(word) > 1 and not word[1:].islower():
               raise ValueError(
                   "The remaining characters of each word must be lowercase."
               )
   
        return value
    
    
    # Filtering Delivery destination more deeply...
    @field_validator("delivery")
    @classmethod
    def validate_job_title(cls, value: str):

        words = value.strip().split()

        for word in words:
            if not word[0].isupper():
                raise ValueError(
                    "Each word must start with an uppercase letter."
                )

            if len(word) > 1 and not word[1:].islower():
                raise ValueError(
                    "The remaining characters of each word must be lowercase."
                )

        return value 
    
    # Including a rule where user can't entry same location
    @model_validator(mode="after")
    def validate_locations(self):

        if self.pickup.lower() == self.delivery.lower():
            raise ValueError(
                "Pickup and delivery locations must be different."
            )

        return self
    
    
    
class Freight_rate_output(BaseModel):
    posted_rate : Annotated[
        float,
        Field(
            ...,
            ge = 1,
            title = 'Posted Rate'
        )
    ]