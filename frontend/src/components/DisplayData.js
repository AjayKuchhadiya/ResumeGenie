import React from 'react';

function DisplayData({ data }) {
  return (
    <div>
      <h2>Extracted Information</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default DisplayData;
