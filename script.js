const btn = document.getElementById("btn");
const fileInput = document.getElementById("fileInput");
const loading = document.getElementById("loading");
const results = document.getElementById("results");

btn.addEventListener("click", async () => {
    const file = fileInput.files[0];
    if (!file) return alert("Please upload a file.");

    const fd = new FormData();
    fd.append("resume", file);

    loading.style.display = "block";
    results.innerHTML = "";

    try {
        const r = await fetch("http://127.0.0.1:5000/evaluate", { method:"POST", body:fd });
        const data = await r.json();
        loading.style.display = "none";

        results.innerHTML = "<pre>" + JSON.stringify(data, null, 2) + "</pre>";
    } catch (e) {
        loading.style.display = "none";
        alert("Backend not running.");
    }
});
