import Visits from "./visits";
import Clicks from "./clicks";
import Layout from "../components/layout";
import VisitorCountChart from "./visits/components/visitor-count-chart";

const Home = () => {

  return (
      <Layout>
          <div style={{ width: '60%', height: '400px', margin: '0 auto' }}>
              <Clicks />
          </div>
            <div style={{ width: '60%', height: '400px', margin: '0 auto' }}>
                <Visits />
            </div>
      </Layout>
  );
};

export default Home;
