// Presentational + interactive row for a single task.
export default function TaskItem({ task, onToggle, onDelete }) {
  return (
    <li className={`task-item ${task.completed ? 'completed' : ''}`}>
      <input
        type="checkbox"
        checked={task.completed}
        onChange={() => onToggle(task)}
        aria-label={`Mark ${task.title} as ${task.completed ? 'incomplete' : 'complete'}`}
      />
      <div className="task-body">
        <div className="task-title-row">
          <span className="task-title">{task.title}</span>
          <span className={`badge priority-${task.priority}`}>{task.priority}</span>
        </div>
        {task.description && <p className="task-desc">{task.description}</p>}
      </div>
      <button className="delete-btn" onClick={() => onDelete(task.id)} aria-label="Delete task">
        ✕
      </button>
    </li>
  )
}
