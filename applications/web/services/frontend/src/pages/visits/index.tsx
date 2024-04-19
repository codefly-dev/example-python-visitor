import { useEffect } from "react";
import Layout from "../../components/layout";
import { useCodeflyContext } from "../providers/codefly.provider";
import VisitorCountChart from "./components/visitor-count-chart";


const Visits = () => {

  const { routing } = useCodeflyContext()

  const markVisit = () => {

    const visitUrl = routing("POST", { application: "backend", service: "visits" }, "/visit")
    fetch(visitUrl,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({})
      });
  }

  useEffect(() => {
    markVisit()
  }, [])


  return (
      <div style={{ width: '60%', height: '400px', margin: '0 auto' }}>
        <VisitorCountChart />
      </div>
  );
};


export default Visits;
