import { useEffect, useRef, useState } from "react";
import Chart from "chart.js/auto";
import CountUp from "react-countup";
import { useCodeflyContext } from "../../providers/codefly.provider";

const VisitorCountChart = ({ shouldYearShow = false, width = '400px', height = '100px' }) => {
    const chartRef = useRef(null);
    const canvasRef = useRef(null);
    const [startCounting, setStartCounting] = useState(false);
    const [visitorVisits, setVisitorVisits] = useState([]);
    const [totalVisits, setTotalVisits] = useState();

    const { routing } = useCodeflyContext()

    useEffect(() => {
        const fetchData = async () => {
            try {
                const url = routing("GET", { application: "python-visitors", service: "visits" }, "/visit/statistics");
                const response = await fetch(url);

                if (!response.ok) {
                    throw new Error("Failed to fetch data");
                }
                const visitorData = await response.json();
                setVisitorVisits(visitorData.visits);
                setTotalVisits(visitorData.total_visits);
                setStartCounting(true);

            } catch (error) {
                console.error("Error fetching visitor data:", error);
            }
        };
        fetchData();
    }, []);

    useEffect(() => {
        const ctx = canvasRef.current;
        if (ctx && visitorVisits && visitorVisits.length > 0) {
            if (chartRef.current) {
                chartRef.current.destroy();
            }
            chartRef.current = new Chart(ctx, {
                type: "bar",
                data: {
                    labels: visitorVisits.map((entry) =>
                        formatDate(entry.date, shouldYearShow)
                    ),
                    datasets: [
                        {
                            label: "Visitor Count",
                            data: visitorVisits.map((entry) => entry.visits),
                            backgroundColor:  "#1D4ED8",
                            barPercentage: 1,
                            categoryPercentage: 1
                        },
                    ],
                },
                options: {
                    animation: false,
                    scales: {
                        x: {
                            grid: {
                                display: false,
                            },
                        },
                        y: {
                            grid: {
                                display: false,
                            },
                            beginAtZero: true,
                            ticks: {
                                stepSize: 10 // Set the step size to 1
                            }
                        },
                    },
                    plugins: {
                        legend: {
                            display: false,
                        },
                    },
                    layout: {
                        padding: 0
                    },
                    elements: {
                        bar: {
                            borderWidth: 0,
                        }
                    },
                    responsive: true,
                    maintainAspectRatio: false,
                },
            });
        }

        return () => {
            if (chartRef.current) {
                chartRef.current.destroy();
            }
        };
    }, [visitorVisits, shouldYearShow]);

    const formatDate = (dateString, shouldShowYear) => {
        const date = new Date(dateString);
        if (shouldShowYear) {
            return date.toLocaleDateString();
        } else {
            return date.toLocaleDateString(undefined, {
                month: "short",
                day: "2-digit",
            });
        }
    };

    return (
        <div className="mt-5 p-6">
            <div className="flex justify-center pt-20 pb-10">
                <h2>Total visits</h2>
            </div>
            <div className="flex justify-center pt-20">
                <CountUp
                    start={startCounting ? 0 : undefined}
                    end={totalVisits}
                    duration={3}
                    style={{fontSize: 200, display: 'flex'}}
                    separator=","
                    className="text-2xl font-bold text-blue-600 mr-2"
                />
            </div>
            <div className="flex justify-center pt-20">
            <canvas
                ref={canvasRef}
                id="visitor-count-chart"
                className="w-full h-auto"
                style={{padding: "30px", fontSize: "40px", borderRadius: '10px', maxHeight: '400px'}}
            />
            </div>


        </div>
    );
};

export default VisitorCountChart;
