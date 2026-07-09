// Thin API client wrapping fetch calls to the FastAPI backend.
// Base URL comes from Vite env (VITE_API_URL), falling back to localhost.
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

async function request(path, options = {}) {
  const res = await fetch(`${API_URL}${path}`, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  })
  if (!res.ok) {
    let detail = `Request failed (${res.status})`
    try {
      const body = await res.json()
      if (body.detail) detail = typeof body.detail === 'string' ? body.detail : JSON.stringify(body.detail)
    } catch {
      /* ignore non-JSON error bodies */
    }
    throw new Error(detail)
  }
  // 204 No Content has no body.
  if (res.status === 204) return null
  return res.json()
}

export const api = {
  listTasks: () => request('/api/tasks'),
  createTask: (task) => request('/api/tasks', { method: 'POST', body: JSON.stringify(task) }),
  updateTask: (id, updates) =>
    request(`/api/tasks/${id}`, { method: 'PUT', body: JSON.stringify(updates) }),
  deleteTask: (id) => request(`/api/tasks/${id}`, { method: 'DELETE' }),
}
