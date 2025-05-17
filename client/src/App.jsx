import { Link, Route, Routes } from "react-router-dom";
import { Bell } from "lucide-react";

import Sidebar from "./components/common/Sidebar";
import ToastMessages from "./components/toast/ToastMessages";
import OverviewPage from "./pages/OverviewPage";
import GroupsPage from "./pages/GroupsPage";
import UsersPage from "./pages/UsersPage";
import SettingsPage from "./pages/SettingsPage";

function App() {
  return (
    <div className="flex bg-[#131417] h-screen text-gray-100 overflow-hidden">
      {/* BG */}
      <div className="fixed inset-0 z-0">
        {/* <div className="absolute inset-0 backdrop-blur-sm" /> */}
      </div>
      <Link to={"https://chiefcoders-newshub.netlify.app"} target="_blank">
        <Bell className="fixed top-5 right-5 z-40 cursor-pointer" />
      </Link>
      <Sidebar />
      <Routes>
        <Route path="/" element={<OverviewPage />} />
        <Route path="/groups" element={<GroupsPage />} />
        <Route path="/messages" element={<UsersPage />} />
        <Route path="/settings" element={<SettingsPage />} />
      </Routes>
      <ToastMessages />
    </div>
  );
}

export default App;
