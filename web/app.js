async function sendContact(ev) {
    ev.preventDefault();

    const number = document.getElementById('number').value;
    const actualBase = document.getElementById('actualBase').value;
    const base = document.getElementById('base').value;
      
    fetch(`https://bases.funkypanda.me/backend?number=${number}&actualBase=${actualBase}&base=${base}`)
    .then(response => response.json())
    .then(data => {
      const answer = data.answer;
      const working = data.working;
      console.log("Answer:", answer);
      console.log("Working:", working);
      displayAnswer(working,answer);
      // Use the answer and working variables as needed
    })
    .catch(error => {
      console.error("Error:", error);
    });
  }

  function displayAnswer(working, answer) {
    const workings = document.getElementById("working");
    workings.innerHTML = ""; // Clear previous list items
    
    for (let i = 0; i < working.length; i++) {
      const listItem = document.createElement("li");
      // listItem.textContent = `Step ${i}: ${working[i].join(", ")}`;
      listItem.textContent = `${working[i][0]} = ${working[i][1]} X ${working[i][2]} + ${working[i][3]}`;
      workings.appendChild(listItem);
    }

    const finalAnswer = document.getElementById("finalAnswer");
    finalAnswer.textContent = `Final answer: ${answer}`
    
    document.getElementById("right").style = "display: none;"
    document.getElementById("answer").style = "display: block;"
  }