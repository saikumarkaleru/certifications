import { useState } from 'react'

const EMPTY = { title: '', description: '', priority: 'medium' }

// Controlled form for creating a new task.
export default function TaskForm({ onCreate }) {
  const [form, setForm] = useState(EMPTY)
  const [submitting, setSubmitting] = useState(false)
  const [error, setError] = useState('')

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!form.title.trim()) {
      setError('Title is required')
      return
    }
    setSubmitting(true)
    setError('')
    try {
      await onCreate(form)
      setForm(EMPTY)
    } catch (err) {
      setError(err.message)
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <form className="task-form" onSubmit={handleSubmit}>
      <div className="form-row">
        <input
          name="title"
          placeholder="What needs doing?"
          value={form.title}
          onChange={handleChange}
          maxLength={200}
          aria-label="Task title"
        />
        <select name="priority" value={form.priority} onChange={handleChange} aria-label="Priority">
          <option value="low">Low</option>
          <option value="medium">Medium</option>
          <option value="high">High</option>
        </select>
        <button type="submit" disabled={submitting}>
          {submitting ? 'Adding…' : 'Add Task'}
        </button>
      </div>
      <textarea
        name="description"
        placeholder="Optional details…"
        value={form.description}
        onChange={handleChange}
        maxLength={1000}
        rows={2}
        aria-label="Task description"
      />
      {error && <p className="error">{error}</p>}
    </form>
  )
}
