import React, {useEffect, useState} from 'react';
import GoogleMapReact from 'google-map-react';

function App() {
  const YOUR_API_KEY = process.env.REACT_APP_GOOGLE_MAP_API_KEY;
  const defaultProps = {
    center: {
      lat: 33.7701,
      lng: -118.1937
    },
    zoom: 1
  };

  const [data, setData] = useState({});

  useEffect(()=>{
    /*const res = combineAllJSON(myData);
    const d = {
      positions:res
    };
    setData(d);*/
  },[]);

  return (
    <div style={{ height: '100vh', width: '100%' }}>
      <h1>Map</h1>
      <GoogleMapReact                 
      bootstrapURLKeys={{key:YOUR_API_KEY}}          
      defaultCenter={defaultProps.center}          
      defaultZoom={defaultProps.zoom}          
      heatmapLibrary={true}          
      heatmap={data}     
      ></GoogleMapReact>
    </div>
  );
}

export default App;
