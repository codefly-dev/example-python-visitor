import Layout from "../../components/layout";
import VisitorCountChart from "./components/visitor-count-chart";

const Visits = () => {
    return (
      <Layout>
        <div style={{width: '60%', height: '400px', margin: '0 auto', border: '1px solid #ccc'}}>
          <VisitorCountChart  />
        </div>
  
      </Layout>
    );
  };
  
  
  export default Visits;