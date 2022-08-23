export const JSONToHeatMapDataSet = (jsonData) => {
    const data = jsonData["data"];
    return data.map((item) => {
        return {
            lat: item.lat,
            lng: item.lon,
            weight: item.carb_total
        };
    });
}

