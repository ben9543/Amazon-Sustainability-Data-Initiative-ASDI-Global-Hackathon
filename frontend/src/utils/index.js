
export const JSONToHeatMapDataSet = (jsonData, option) => {
    if(option === null) return null;
    const data = jsonData["data"];
    return data[0]["0"].map((item) => {
        return { 
            lat: item.lat,
            lng: item.lon,
            weight: item.carb_total
        } 
    });
}

