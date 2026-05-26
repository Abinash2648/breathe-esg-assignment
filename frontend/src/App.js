import { useEffect, useState } from "react";
import axios from "axios";

function App() {

  const [records, setRecords] = useState([]);
  const [file, setFile] = useState(null);

  useEffect(() => {

    axios.get("http://127.0.0.1:8000/api/emissions/")
      .then((response) => {
        setRecords(response.data);
      });

  }, []);

  // Upload CSV
  const handleUpload = async () => {

    if (!file) {
      alert("Please select a CSV file");
      return;
    }

    const formData = new FormData();

    formData.append("file", file);

    try {

      await axios.post(
        "http://127.0.0.1:8000/api/upload-csv/",
        formData
      );

      alert("CSV Uploaded Successfully");

      window.location.reload();

    } catch (error) {

      console.log(error);

      alert("Upload Failed");
    }
  };

  // Dashboard Summary
  const totalEmission = records.reduce(
    (sum, item) => sum + item.total_emission,
    0
  );

  const scope1 = records.filter(
    item => item.scope_type === "Scope 1"
  ).length;

  const scope2 = records.filter(
    item => item.scope_type === "Scope 2"
  ).length;

  const scope3 = records.filter(
    item => item.scope_type === "Scope 3"
  ).length;

  return (

    <div className="container mt-5">

      <h1 className="text-center mb-5">
        ESG Emission Dashboard
      </h1>

      {/* Upload CSV */}

      <div className="card p-4 mb-5 shadow">

        <h3 className="mb-3">
          Upload CSV File
        </h3>

        <input
          type="file"
          className="form-control mb-3"
          onChange={(e) => setFile(e.target.files[0])}
        />

        <button
          className="btn btn-primary"
          onClick={handleUpload}
        >
          Upload CSV
        </button>

      </div>

      {/* Dashboard Summary */}

      <div className="row mb-5">

        <div className="col-md-3">
          <div className="card bg-dark text-white shadow">
            <div className="card-body">
              <h5>Total Records</h5>
              <h2>{records.length}</h2>
            </div>
          </div>
        </div>

        <div className="col-md-3">
          <div className="card bg-success text-white shadow">
            <div className="card-body">
              <h5>Total Emissions</h5>
              <h2>{totalEmission.toFixed(2)}</h2>
            </div>
          </div>
        </div>

        <div className="col-md-2">
          <div className="card bg-primary text-white shadow">
            <div className="card-body">
              <h5>Scope 1</h5>
              <h2>{scope1}</h2>
            </div>
          </div>
        </div>

        <div className="col-md-2">
          <div className="card bg-warning text-dark shadow">
            <div className="card-body">
              <h5>Scope 2</h5>
              <h2>{scope2}</h2>
            </div>
          </div>
        </div>

        <div className="col-md-2">
          <div className="card bg-danger text-white shadow">
            <div className="card-body">
              <h5>Scope 3</h5>
              <h2>{scope3}</h2>
            </div>
          </div>
        </div>

      </div>

      {/* Emission Cards */}

      <div className="row">

        {
          records.map((item) => (

            <div className="col-md-4 mb-4" key={item.id}>

              <div className="card shadow h-100">

                <div className="card-body">

                  <h3 className="card-title">
                    {item.category}
                  </h3>

                  <p>
                    <strong>Scope:</strong> {item.scope_type}
                  </p>

                  <p>
                    <strong>Raw Value:</strong> {item.raw_value}
                  </p>

                  <p>
                    <strong>Emission Factor:</strong> {item.emission_factor}
                  </p>

                  <p className="text-success fw-bold">
                    Total Emission:
                    {" "}
                    {item.total_emission.toFixed(2)}
                  </p>

                </div>

              </div>

            </div>

          ))
        }

      </div>

    </div>

  );
}

export default App;