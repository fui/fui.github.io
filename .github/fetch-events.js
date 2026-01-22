const fs = require("fs");

const peoplyUrl = "https://api.peoply.app/events";
const params = new URLSearchParams({
  organizationId: "5f316c2d-e6ec-4f38-a2e5-cd66ab785177",
  orderDirection: "desc",
  take: 5,
  skip: 0,
});

const url = `${peoplyUrl}?${params}`;
const eventIdFile = "_data/eventId.txt";

let prevEventId = "";

if (fs.existsSync(eventIdFile)) {
  prevEventId = fs.readFileSync(eventIdFile, "utf-8").trim();
};

fetch(url)
  .then((res) => res.json())
  .then((data) => {
    // console.log("Fetched events:", data);

    if (!data || data.length === 0) {
      console.log("No data returned from Peoply.")
      process.exit(0);
    };

    // Accesss latest event ID
    const latestEvent = data[0];
    const latestEventId = latestEvent.id;

    // Stop if no new event
    if (latestEventId === prevEventId) {
      console.log("No new events in Peoply.");
      process.exit(0);
    };

    // New event found
    console.log("New event added in Peoply.");
    fs.writeFileSync(eventIdFile, latestEventId);

    // Adjust event time to follow timezone in Norway:
    const updatedData = data.map(event => {
      const date = new Date(event.startDate);
      const updatedStartDate = date.toLocaleString("no-NB", { timeZone: "Europe/Oslo" });

      return {...event, startDate: updatedStartDate };
    })

    fs.writeFileSync("_data/events.json", JSON.stringify(updatedData, 2));
    // console.log("Events written to _data/events.json");

    process.exit(1);
  })
  .catch((err) => {
    console.error("Failed to fetch events:", err);
    process.exit(1);
  });

