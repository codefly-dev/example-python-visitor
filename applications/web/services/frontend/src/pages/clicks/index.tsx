import {useEffect, useState} from "react";
import {useCodeflyContext} from "../providers/codefly.provider";
import CountUp from "react-countup";


const Clicks = () => {

    const doClick = () => {
        const visitUrl = routing("POST", {application: "backend", service: "clicks"}, "/click")
        const resp = fetch(visitUrl, {
            method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({})
        });
        resp.then((value) => {
            const response = value.json();
            setTotalClicks(response["count"]);
        });
    };

    const [startCounting, setStartCounting] = useState(false);
    const [totalClicks, setTotalClicks] = useState();

    const {routing} = useCodeflyContext()

    useEffect(() => {
        const fetchData = async () => {
            try {
                const url = routing("GET", {application: "backend", service: "clicks"}, "/clicks");
                const response = await fetch(url);

                if (!response.ok) {
                    throw new Error("Failed to fetch data");
                }
                const clickData = await response.json();
                setTotalClicks(clickData.counts);
                setStartCounting(true);

            } catch (error) {
                console.error("Error fetching visitor data:", error);
            }
        };
        fetchData();
    }, []);

    return (<div className="mt-5 p-6">
            <div className="flex justify-center pt-20">
                <CountUp
                    start={startCounting ? 0 : undefined}
                    end={totalClicks}
                    duration={3}
                    style={{fontSize: 200, display: 'flex'}}
                    separator=","
                    className="text-2xl font-bold text-blue-600 mr-2"
                />
            </div>
            <div className="flex justify-center">
                <button
                    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-5"
                    onClick={doClick}
                >
                    Click Me
                </button>
            </div>
        </div>);
};


export default Clicks;
