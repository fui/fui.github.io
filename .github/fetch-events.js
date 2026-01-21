const fs = require("fs");

const peoplyUrl = "https://api.peoply.app/events";
const params = new URLSearchParams({
  organizationId: "5f316c2d-e6ec-4f38-a2e5-cd66ab785177",
  orderDirection: "desc",
  take: 5,
  skip: 0,
});

const url = `${peoplyUrl}?${params}`;
let event;

// Checks if a new event has occured in Peoply:
const hasNewEvent = (event) => {
  console.log("Fetched latest event:", event);

  const currentDate = new Date().toLocaleString("no-NB", { timeZone: "Europe/Oslo" });
  const eventDate = new Date(event.startDate).toLocaleString("no-NB", { timeZone: "Europe/Oslo" });

  console.log("Current: ", currentDate);
  console.log("Event: ", eventDate);

  return currentDate < eventDate;
};

fetch(url)
  .then((res) => res.json())
  .then((data) => {
    console.log("Fetched events:", data);

    // Adjust event time to follow timezone in Norway:
    const updatedData = data.map(event => {
      const date = new Date(event.startDate);
      const updatedStartDate = date.toLocaleString("no-NB", { timeZone: "Europe/Oslo" });

      return {...event, startDate: updatedStartDate };
    })

    fs.writeFileSync("_data/events.json", JSON.stringify(updatedData, 2));
    console.log("Events written to _data/events.json");

    // Get first event from Peoply as events are ordered by date
    const values = Object.values(updatedData);
    event = values[0];
    hasNewEvent(event);
  })
  .catch((err) => {
    console.error("Failed to fetch events:", err);
    process.exit(1);
  });

