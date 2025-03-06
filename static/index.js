let views=document.querySelectorAll('.views');
let searchinput=document.querySelector('#searchinput')
let maps=document.querySelectorAll('.maps');
for(let view of views){
  
  view.addEventListener("click",()=>{
    let name=view.id.split(" ")
    console.log(name)
    latitude=parseFloat(name[0])
    longitude=parseFloat(name[1])
  console.log(latitude,longitude)
    // Initialize the Map
    let map = L.map('map').setView([latitude, longitude], 18);

    // Add OpenStreetMap Layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    // Add Marker to the Location
    let marker = L.marker([latitude, longitude]).addTo(map);
    marker.bindPopup("<b>Your Location</b><br>Delhi").openPopup();

    // Add Navigation Link
    marker.on("click",()=>{
        window.open(`https://www.google.com/maps/dir/?api=1&destination=${latitude},${longitude}`, '_blank');
    });
  })
}