import "./styles.css";
// import ReactDOM from "react-dom/client";
import { StyledEngineProvider } from "@mui/material/styles";
import MainTable from "./mainTable";

export default function App() {
  return (
    <div className="App">
      <h1>Scooby-Doo</h1>
      <label for="series_name">Series Names filters:</label>

      <select name="series_name" id="series_name">
        <option value="Where_Are_You!">Scooby Doo, Where Are You!</option>
        <option value="dave">Dave</option>
        <option value="pumpernickel">Pumpernickel</option>
        <option value="reeses">Reeses</option>
      </select>
      <StyledEngineProvider injectFirst>
        <MainTable />
      </StyledEngineProvider>
    </div>
  );
}
