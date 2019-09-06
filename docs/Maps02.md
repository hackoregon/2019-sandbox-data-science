# Sandbox Census Maps for PDX and DC

Each of these maps is 2 maps: one for Portland, and one for D.C. We have two "major" topics, and 6 maps, or "minor topics" for each one:

        CITY: PDX and DC
              /       \
        Maps 1-6     Maps 1-6

The endpoints are split by city; I'm not sure where the Opportunity Zones endpoints ended up (Ed did those), and our two endpoints for the census layers are here:

http://service.civicpdx.org/sandbox/api/Dataset045Pdxs/
http://service.civicpdx.org/sandbox/api/Dataset045Dcs/


### Map 1: Racial Diversity and Opportunity Zones

#### Primary (Default) View:

* Race Share TBD - one of the 2017 layers below.
* Opportunity Zones -- A boolean value that shows only 1 = opp zone; 0 = not opp zone. We'll skip mapping eligibility requirements here.

*THOUGHT*: We could have a Map #7 that overlaps the actual opportunity zones for the city with the eligibility requirements. I'll put that below.

#### Secondary Views/Layers available:

* WhiteShare_90
* WhiteShare_00
* WhiteShare_10
* WhiteShare_17
* BlackShare_90
* BlackShare_00
* BlackShare_10
* BlackShare_17
* HispShare_90
* HispShare_00
* HispShare_10
* HispShare_17
* AsOthShare_90
* AsOthShare_00
* AsOthShare_10
* AsOthShare_17


#### Visualization Types:

For all 16 Race layers:

Choropleth Map - Standard
- OPACITY - whatever works to show this + opportunity zones layered on top
- SCALE TYPE: equal; can we do more continuous bins? (by 1%), given that some proportions are always less than 10%;
    maybe a major color bin at the 10% mark, and then a minor color bin for each 1% marker along that scale as well.
- CIVIC COLOR:

  * our choice; I like ocean - pick whatever makes this particular set of 6 packages stand  out as "Sandbox Team" - it can be uniform across the maps, or shift slightly with different variables - I leave this completely up to you.
  * Maybe we can also shift colors by one of the variables - i.e. either year or race? That way the groupings are a bit more visual


- FIELD NAME: Let's match the Boston maps here, e.g. "Race: Share White" / "Race: Share Black/ Race: Share Hispanic / Race: Share Asian / Other" plus the year

For Opportunity Zones:
- OPACITY - it needs to be transparent so the census data below can be seen

- SCALE TYPE: boolean/categorical

- CIVIC COLOR:

  * your choice; make 100% transparent for opp zone = 0, and then a single color with transparency for opp zone = 1.

- FIELD NAME: "Opportunity Zone"



### Map 2: Affluence and Income Inequality

#### Primary View(s):

* MedInc_17
* ChInc_9017
* Opportunity Zones

#### Secondary Views/Layers available:

Group 1 Layers
* ChInc_9017
* ChInc_0017
* ChInc_1017

Group 2 Layers
* MedInc_90
* MedInc_00
* MedInc_10
* MedInc_17

Opportunity Zones Layer

Other variables available:

* Metropolitan Area Median Incomes/Change in Incomes for DC and for PDX. Could duplicate this map with those data as well for another map.

#### Visualization Types:

For Median Income Layers:

Choropleth Map - Standard
- OPACITY - whatever works to show this + opportunity zones layered on top
- SCALE TYPE: equal
- CIVIC COLOR: your choice/ what works best with these 6 maps to be both "Sandbox Team" uniform but also vary by map type. Should be different than the "Share" variables at least by a little bit, as these values are continuous dollar amounts
- FIELD NAME: Let's match the Boston maps here; "Median Income" and "Year"


For Change in Median Income Layers:

Bubble Map - Diverging
- OPACITY - whatever works to show this
- SCALE TYPE: threshold (will have + and - values)
- CIVIC COLOR:
  * your choice/ what works best with these 6 maps to be both "Sandbox Team" uniform but also vary by map type.
  * The size of the bubble should reflect divergence from 0; this is a change variable. The color should reflect positive vs negative values
- FIELD NAME: "Change in Median Income from year to year"


For Opportunity Zones:

See Map #1 for same settings (categorial choropleth)


### Map 3: Concentrated Poverty

#### Primary View (Default):

* PovRate_17
* Opportunity Zones

#### Secondary Views/Layers available:

* PovRate_90
* PovRate_00
* PovRate_10
* PovRate_17

* Opportunity Zones

#### Visualization Types:

For Poverty Rate Layers:

Choropleth Map - Standard
- OPACITY - whatever works to show this + opportunity zones layered on top
- SCALE TYPE: equal
- CIVIC COLOR: your choice/ what works best with these 6 maps to be both "Sandbox Team" uniform but also vary by map type. Should be more similar to Share values, as these are proportional (0 to 1)
- FIELD NAME: "Poverty Rate" and "Year"


For Opportunity Zones:

See Map #1 for same settings (categorial choropleth)




### Map 4: Home Values

#### Primary View(s):

* MedHomeVal_17
* Opportunity Zones

#### Secondary Views/Layers available:

* MedHomeVal_90
* MedHomeVal_00
* MedHomeVal_10
* MedHomeVal_17

* Opportunity Zones

#### Visualization Types:

For Home Value Layers:

Choropleth Map - Standard
- OPACITY - whatever works to show this + opportunity zones layered on top
- SCALE TYPE: equal
- CIVIC COLOR: your choice/ what works best with these 6 maps to be both "Sandbox Team" uniform but also vary by map type. This is a dollar amount.
- FIELD NAME: "Median Home Value" and "Year"


For Opportunity Zones:

See Map #1 for same settings (categorial choropleth)





### Map 5: Cost-burdened renters

#### Primary View(s):

* MedInc_17
* RentCBShare_17
* Opportunity Zones


#### Secondary Views/Layers available:

Group 1 (Median Income)

* MedInc_90
* MedInc_00
* MedInc_10
* MedInc_17

Group 2 (Cost-Burdened Renters)

* RentCBShare_90
* RentCBShare_00
* RentCBShare_10
* RentCBShare_17

Group 3

* Opportunity Zones

Other:

Metro RentCBShare and Change RentCBhare are also available.


#### Visualization Types:

For Median Income Layers:

Match the layer from Map #2


For Cost Burdened Renters Share Layers:
(paying more than 30 percent of their income in rent)

Bubble Map - Standard
- OPACITY - whatever works to show this
- SCALE TYPE: equal
- CIVIC COLOR:
  * your choice/ what works best with these 6 maps to be both "Sandbox Team" uniform but also vary by map type.
  * The size and color of the bubble should reflect the value from 0-1 (this is proportional)
- FIELD NAME: "Share of Cost-Burdened Renters" or "Share of Renters who spend more than 30% of their income on rent"


For Opportunity Zones:

See Map #1 for same settings (categorial choropleth)









### Map 6: Gentrifying Neighborhoods

#### Primary View(s):

* ChRent_1017
* ChBachShare_1017
* Opportunity Zones

#### Secondary Views/Layers available:

This is tricky; we only have Change in Rent here at present (matching Boston). But, I think perhaps we should find a way to represent Median Rent as well so that Change in Rent is clear. Do you have ideas for how to represent a third variable? Here are the fields, if so:

* MedRentVal_90
* MedRentVal_00
* MedRentVal_10
* MedRentVal_17


Group 1: Change in Rent

* ChRent_9017
* ChRent_0017
* ChRent_1017

Group 2: Change in People who have Bachelor's Degree
* ChBachShare_9017
* ChBachShare_0017
* ChBachShare_1017

* Opportunity Zones

* Note: Metro ChRent and ChBachShare values are also available.

#### Visualization Types:

For Change in Rent Layers:

Choropleth Map - Standard
- OPACITY - whatever works to show this + opportunity zones layered on top
- SCALE TYPE: equal
- CIVIC COLOR: your choice/ what works best with these 6 maps to be both "Sandbox Team" uniform but also vary by map type. Should be more similar to Share values, as these are proportional (0 to 1)
- FIELD NAME: "Change in Median Rent" and "Year to Year"


For Change in Bachelors Degree Layers:
(paying more than 30 percent of their income in rent)

Bubble Map - Standard
- OPACITY - whatever works to show this
- SCALE TYPE: equal
- CIVIC COLOR:
  * your choice/ what works best with these 6 maps to be both "Sandbox Team" uniform but also vary by map type.
  * The size and color of the bubble should reflect the value from 0-1 (this is proportional)
- FIELD NAME: "Change in Share of People with a Bachelor's Degree from year to year"


For Opportunity Zones:

See Map #1 for same settings (categorial choropleth)




### Map 7: Opportunity Zones and Elibilitity requirements

#### Primary View(s):

* Opportunity Zones Eligibility Requirements
* Opportunity Zones

#### Visualization Types:

For Eligibility Requirements:

Categorical Choropleth with the values represented as different colors.


For Opportunity Zones:

See Map #1 for same settings (categorial choropleth)
