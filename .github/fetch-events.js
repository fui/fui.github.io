const fs = require("fs");

const peoplyUrl = "https://api.peoply.app/events";
const params = new URLSearchParams({
  organizationId: "5f316c2d-e6ec-4f38-a2e5-cd66ab785177",
  orderDirection: "desc",
  take: 5,
  skip: 0,
});

const url = `${peoplyUrl}?${params}`;

fetch(url)
  .then((res) => res.json())
  .then((data) => {
    console.log("Fetched events:", data);

    // Adjust event time to follow timezone in Norway:
    data.forEach(event => {
      const date = new Date(event.startDate);
      event.startDate = date.toLocaleString("nb-NO", {
        timeZone: "Europe/Oslo"
      });
    });

    fs.writeFileSync("_data/events.json", JSON.stringify(data, 2));
    console.log("Events written to _data/events.json");
  })
  .catch((err) => {
    console.error("Failed to fetch events:", err);
    process.exit(1);
  });
