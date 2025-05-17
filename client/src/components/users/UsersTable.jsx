import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { Search, X } from "lucide-react";

const userData = [
  {
    userId: 800639016,
    Message: `MEDICATIONS👩‍❤️‍💋‍👨
➡️Xanax Bars 1,2mg 
➡️Alprazolam 1mg 
➡️Diazepam 10mg 
➡️Clonazepam 2mg 
➡️Lorazepam 2.5mg 
➡️Zopiclon 7.5mg 
➡️Zolpidem 10mg 
➡️Soa-kuur chlamydia 
➡️Tramadol. 50mg 
➡️Tramadol 100mg 
➡️Tramadol 200mg 
➡️Modafinil 200mg 
➡️armodafinil 150mg 
➡️Pregabaline 300mg 
➡️Ritalin 10mg 
➡️Temazepam 20mg 
➡️Oxycodone 80/120mg
➡️ KAMAGRA 100 mg
➡️ Cenforce 200 mg
➡️ Sextreme Sildalis 160mg
➡️Vidalista 60 mg WEEKENDPIL
➡️ COBRA 120mg`,
    message_id: 12333,
    UserName: "Arvind .V",
    senderName: "Arvinds21",
    RiskLvl: "Low",
    Chat_Id: "2241003403",
  },
  {
    userId: 4562789526,
    Message: `G@nja testing`,
    message_id: 12334,
    UserName: "null",
    RiskLvl: "High",
    senderName: "Mr Han",
    Chat_Id: "4562789526",
    remarks: "NA",
  },
  {
    userId: 452368700,
    Message: `🍁WEED🍁
➡️cali
➡️haze
➡️kush
📢more in channel    `,
    message_id: 12336,
    UserName: "ArvindValliore",
    senderName: "Arpan",
    RiskLvl: "High",
    Chat_Id: "1530045679",
  },
  {
    userId: 8756231526,
    Message: `👍VAPES 5k-12k 👍
RandM 7k
-RandM 9k
-RandM 12k`,
    message_id: 12337,
    UserName: "Arpan87",
    senderName: "Hardik",
    RiskLvl: "Low",
    Chat_Id: "6511230007",
  },
  {
    userId: 235684219,
    Message: `Gelato Cake 🍰 
9.5/10 👃 
800
Dante Inferno 
9/10 👃 
750
Boston Runtz 
9/10 👃 
775
Headhunters 
9/10 👃 
800`,
    message_id: 12339,
    senderName: "Prerit",
    UserName: "null",
    RiskLvl: "High",
    Chat_Id: "235684219",
    remarks: "NA",
  },
];

const UsersTable = () => {
  const [searchTerm, setSearchTerm] = useState("");
  const [filteredUsers, setFilteredUsers] = useState(userData);
  const [selectedMessage, setSelectedMessage] = useState(null);

  useEffect(() => {
    const timeout = setTimeout(() => {
      const term = searchTerm.toLowerCase();
      const filtered = userData.filter(
        (user) =>
          user.Message.toLowerCase().includes(term) ||
          String(user.message_id).includes(term) ||
          user.UserName.toLowerCase().includes(term)
      );
      setFilteredUsers(filtered);
    }, 300);
    return () => clearTimeout(timeout);
  }, [searchTerm]);

  return (
    <motion.div
      className="bg-[#1E1F26] shadow-lg rounded-xl p-6 border border-gray-700"
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: 0.2 }}
    >
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-xl font-semibold text-gray-100">Messages</h2>
        <div className="relative">
          <input
            type="text"
            placeholder="Search messages..."
            className="bg-gray-700 text-white placeholder-gray-400 rounded-lg pl-10 pr-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
          <Search className="absolute left-3 top-2.5 text-gray-400" size={18} />
        </div>
      </div>

      <div className="overflow-x-auto">
        <table className="min-w-full divide-y divide-gray-700">
          <thead>
            <tr>
              {[
                "Message",
                "Message ID",
                "User ID",
                "Username",
                "Chat ID",
                "Remarks",
              ].map((header) => (
                <th
                  key={header}
                  className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider"
                >
                  {header}
                </th>
              ))}
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-700">
            {filteredUsers.length > 0 ? (
              filteredUsers.map((user) => (
                <motion.tr
                  key={user.userId}
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  transition={{ duration: 0.3 }}
                  className="hover:bg-gray-800 cursor-pointer"
                  onClick={() => setSelectedMessage(user.Message)}
                >
                  <td className="px-6 py-4 whitespace-nowrap text-gray-300 max-w-[200px] truncate overflow-hidden">
                    {user.Message}
                  </td>
                  <td className="px-6 py-4 text-gray-300">{user.message_id}</td>
                  <td className="px-6 py-4 text-gray-300">{user.userId}</td>
                  <td className="px-6 py-4 text-gray-300">
                    {user.senderName || "N/A"}
                  </td>
                  <td className="px-6 py-4 text-gray-300">{user.Chat_Id}</td>
                  <td className="px-6 py-4 text-gray-300">
                    {user.remarks || "N/A"}
                  </td>
                </motion.tr>
              ))
            ) : (
              <tr>
                <td colSpan="6" className="text-center py-6 text-gray-400">
                  No messages found.
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
      {selectedMessage && (
        <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-100">
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.2 }}
            className="bg-gray-800 p-6 rounded-lg shadow-lg max-w-lg w-full text-white "
          >
            <div className="flex justify-between items-center mb-4">
              <h3 className="text-lg font-semibold">Full Message</h3>
              <X
                className="cursor-pointer"
                onClick={() => setSelectedMessage(null)}
              />
            </div>
            <p className="text-gray-300">{selectedMessage}</p>
          </motion.div>
        </div>
      )}
    </motion.div>
  );
};

export default UsersTable;
