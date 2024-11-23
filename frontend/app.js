document.getElementById('journalForm').addEventListener('submit', async (event) => {
    event.preventDefault();

    const journalEntry = document.getElementById('journalEntry').value;

    try {
      const response = await fetch('http://127.0.0.1:5000/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: journalEntry })
      });

      const data = await response.json();

      // Display analysis
      document.getElementById('sentiment').textContent = `Analysis: ${data.analysis}`;

      // Display recommendations
      document.getElementById('recommendations').innerHTML = `<ul>${data.recommendations.split('\n').map(item => `<li>${item}</li>`).join('')}</ul>`;
    } catch (error) {
      console.error('Error:', error);
      // Handle errors gracefully
    }
});
