import React from "react";
import Table from 'react-bootstrap/Table';

const DisplayData = ({ data }) => {
  // Ensure data is an object before rendering
  if (!data || typeof data !== 'object') {
    return null; // or a fallback UI like a loading spinner or message
  }

  return (
    <div>
      <h3>Extracted Information</h3>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>Field</th>
            <th>Value</th>
          </tr>
        </thead>
        <tbody>
          {Object.entries(data).map(([key, value]) => (
            <tr key={key}>
              <td>{key}</td>
              <td>{typeof value === 'object' ? JSON.stringify(value) : value}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export default DisplayData;
