import React, { useEffect, useState } from "react";
import axios from "axios";
import { useParams, useNavigate, Link } from "react-router-dom";
import Loading from "./Loading";

const EditTask = () => {
  const { id } = useParams();
  const [task, setTask] = useState({ title: "", description: "" });
  const [loading, setLoading] = useState(false);
  const [initialTask, setInitialTask] = useState({
    title: "",
    description: "",
  });
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const fetchTask = async () => {
      setLoading(true);
      try {
        const response = await axios.get(
          `http://localhost:5000/api/tasks/${id}`
        );
        setTask({
          title: response.data.title,
          description: response.data.description,
        });
        setInitialTask({
          title: response.data.title,
          description: response.data.description,
        });
      } catch (error) {
        setError("Error fetching task. Please try again.");
        console.error("Fetch task error: ", error);
        navigate("/");
      } finally {
        setLoading(false);
      }
    };
    fetchTask();
  }, [id, navigate]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage(""); // Reset message
    setError(""); // Reset error

    // Check if the task has been changed
    if (
      task.title === initialTask.title &&
      task.description === initialTask.description
    ) {
      setError("No changes detected to update.");
      return;
    }

    const confirmUpdate = window.confirm(
      "Are you sure you want to update this task?"
    );
    if (confirmUpdate) {
      setLoading(true);
      try {
        await axios.put(`http://localhost:5000/api/tasks/${id}`, task);
        alert("Task updated successfully!");
        // Optionally reset the form values
        setInitialTask(task);
        setTask({ title: "", description: "" }); // Clear fields after update
        navigate("/");
      } catch (error) {
        const message =
          error.response?.data?.error ||
          "Error updating task. Please try again.";
        setError(message);
        console.error("Update task error: ", error);
      } finally {
        setLoading(false);
      }
    } else {
      setError("Task update canceled.");
    }
  };

  if (loading) {
    return <Loading />;
  }

  return (
    <div className="p-6 bg-slate-100 min-h-[100vh]">
      <section className="flex justify-between items-center flex-wrap">
        <h1 className="text-2xl mb-4">Edit Task</h1>
        <Link to="/">
          <button className="bg-blue-500 text-white px-4 py-1 rounded">
            Back
          </button>
        </Link>
      </section>
      {error && <p className="text-red-500">{error}</p>}
      {message && <p className="text-green-500">{message}</p>}
      <form onSubmit={handleSubmit} className="bg-white p-4 rounded shadow-md">
        <div className="mb-4">
          <label className="block mb-1">Title</label>
          <input
            type="text"
            value={task.title}
            onChange={(e) => setTask({ ...task, title: e.target.value })}
            className="border p-2 w-full"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block mb-1">Description</label>
          <textarea
            value={task.description}
            onChange={(e) => setTask({ ...task, description: e.target.value })}
            className="border p-2 w-full"
            required
          />
        </div>
        <button
          type="submit"
          className="bg-green-500 text-white px-4 py-2 rounded"
        >
          Update Task
        </button>
      </form>
    </div>
  );
};

export default EditTask;
