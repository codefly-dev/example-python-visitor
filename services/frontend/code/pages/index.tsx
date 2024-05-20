import Visits from "./visits";
import Clicks from "./clicks";
import Layout from "../components/layout";
import VisitorCountChart from "./visits/components/visitor-count-chart";

const Home = () => {

  return (
      <Layout>
          {/*<div >*/}
          {/*    <Clicks />*/}
          {/*</div>*/}
            <div>
                <Visits />
            </div>
      </Layout>
  );
};

export default Home;
