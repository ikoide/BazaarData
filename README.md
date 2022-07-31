# Hypixel Bazaar API

The aim of this project is to provide historical data for the items on the Hypixel bazaar. 

## API

### Parameters

**Item Name: ** The name of an item listed on the Hypixel bazaar.
**Limit: ** The the number of historic results you want for the query.
**Offset: ** The value the query should be offset by from the first index.

### Example Request

**GET** https://bazaar.sewer.fail/api/v1/item/STOCK_OF_STONKS?limit=4&offset=0

`200 OK`

``` json
{
    "name": "STOCK_OF_STONKS",
    "sellPrice": [481147.1278165503, 481147.1278165503, 481147.2839011925, 481147.2839011925],
    "sellVolume": [35535, 35535, 35706, 35706],
    "sellMovingWeek": [20265, 20265, 20112, 20112],
    "sellOrders": [380, 380, 381, 381],
    "buyPrice": [519998.69540, 519998.4, 519997.9, 519997.7],
    "buyVolume": [7732, 8028, 7537, 7774],
    "buyMovingWeek": [20492, 20492, 20508, 20508],
    "buyOrders": [45, 47, 43, 45],
    "datetimes": ["2022-07-31 17:48:36.122000", "2022-07-31 17:48:36.122000", "2022-07-31 18:09:44.794000", "2022-07-31 18:10:15.634000"]
}
```

## Donate
XMR: 8BRD4Z8Z1mFgEdnfLXpmSjcN4VVfkgSQE5PUNrKudWi7hyaCmRSAfEUCVe9duoH6SfdcF4QaFZ4AHCwx1KBXAEgjR1xaqaW
