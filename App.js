// File: client/src/App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    axios.get('/api/tasks')
      .then(response => setTasks(response.data))
      .catch(error => console.error('Error fetching tasks:', error));
  }, []);

  return (
    <div className="App">
      <h1>SmartScheduler</h1>
      <ul>
        {tasks.map(task => (
          <li key={task.id}>{task.name} - {task.due_date}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
