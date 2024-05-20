import {useEffect, useState} from "react";
import {useCodeflyContext} from "../providers/codefly.provider";
import CountUp from "react-countup";

const Clicks = () => {

    const [isLoading, setIsLoading] = useState(true);
    const doClick = () => {
        const visitUrl = routing("POST", {application: "backend", service: "clicks"}, "/click")
        const resp = fetch(visitUrl, {
            method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({})
        });
        resp.then((value) => {
            const response = value.json();
            response.then((data) => {
                setTotalClicks(data["count"]);
            });
        });
    };

    const [totalClicks, setTotalClicks] = useState(null);

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
                setTotalClicks(clickData.count);
                setIsLoading(false);

            } catch (error) {
                console.error("Error fetching visitor data:", error);
            }
        };
        fetchData();
    }, []);

    return (
        <div className="mt-5 p-6">
            <div className="flex justify-center pt-20">
                {isLoading ? (
                    <p>Loading...</p> // Display a loading message
                ) : (
                    <CountUp
                        start={totalClicks}
                        end={totalClicks}
                        duration={0}
                        style={{fontSize: 200, display: 'flex'}}
                        separator=","
                        className="text-2xl font-bold text-blue-600 mr-2"
                    />
                )}
                <button
                    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-5"
                    onClick={doClick}
                >
                    Click Me
                </button>
            </div>
        </div>
    );
};
export default Clicks;
