const url = 'http://127.0.0.1:8000/api_all/';

const getdata = async()=>{
    console.log("fetching data .....");
    let response = await fetch(url);
    let data = await response.json();
    console.log(data);
}
getdata()