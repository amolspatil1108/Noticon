import React, { useEffect, useState } from 'react';

function App() {
  const [services, setServices] = useState([]);

  useEffect(() => {
    fetch('/api/services')
      .then((res) => res.json())
      .then(setServices);
  }, []);

  return (
    <div className="container">
      <h1 className="title">Service Grid</h1>
      <div className="grid">
        {services.map((service) => (
          <div className="card" key={service.name}>
            <img src={service.logo} alt={service.name} className="logo" />
            <div className="name">{service.name}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;