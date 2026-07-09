import { useEffect, useMemo, useState } from 'react'
import { api } from './api'
import TaskForm from './components/TaskForm'
import TaskItem from './components/TaskItem'

export default function App() {
  const [tasks, setTasks] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [filter, setFilter] = useState('all') // all | active | completed

  // Load tasks once on mount.
  useEffect(() => {
    loadTasks()
  }, [])

  async function loadTasks() {
    setLoading(true)
    setError('')
    try {
      const data = await api.listTasks()
      setTasks(data)
    } catch (err) {
      setError(`Could not load tasks: ${err.message}`)
    } finally {
      setLoading(false)
    }
  }

  async function handleCreate(form) {
    const created = await api.createTask(form)
    setTasks((prev) => [created, ...prev])
  }

  async function handleToggle(task) {
    const updated = await api.updateTask(task.id, { completed: !task.completed })
    setTasks((prev) => prev.map((t) => (t.id === updated.id ? updated : t)))
  }

  async function handleDelete(id) {
    await api.deleteTask(id)
    setTasks((prev) => prev.filter((t) => t.id !== id))
  }

  const visibleTasks = useMemo(() => {
    if (filter === 'active') return tasks.filter((t) => !t.completed)
    if (filter === 'completed') return tasks.filter((t) => t.completed)
    return tasks
  }, [tasks, filter])

  const remaining = tasks.filter((t) => !t.completed).length

  return (
    <div className="app">
      <header className="app-header">
        <h1>Task Tracker</h1>
        <p className="subtitle">FastAPI + React full-stack demo</p>
      </header>

      <main className="container">
        <TaskForm onCreate={handleCreate} />

        <div className="toolbar">
          <span className="count">{remaining} task{remaining !== 1 ? 's' : ''} left</span>
          <div className="filters">
            {['all', 'active', 'completed'].map((f) => (
              <button
                key={f}
                className={filter === f ? 'active' : ''}
                onClick={() => setFilter(f)}
              >
                {f}
              </button>
            ))}
          </div>
        </div>

        {error && <p className="error banner">{error}</p>}

        {loading ? (
          <p className="muted">Loading…</p>
        ) : visibleTasks.length === 0 ? (
          <p className="muted">No tasks here yet. Add one above!</p>
        ) : (
          <ul className="task-list">
            {visibleTasks.map((task) => (
              <TaskItem
                key={task.id}
                task={task}
                onToggle={handleToggle}
                onDelete={handleDelete}
              />
            ))}
          </ul>
        )}
      </main>

      <footer className="app-footer">
        <span>Data served by FastAPI · SQLite</span>
      </footer>
    </div>
  )
}
