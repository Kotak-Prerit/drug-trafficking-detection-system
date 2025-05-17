import { motion } from "framer-motion";
import { Edit, Search, Trash2 } from "lucide-react";
import { useState } from "react";

const PRODUCT_DATA = [
  {
    id: 1,
    name: "trafficking",
    Channel: "Channel",
    members: 348,
    CreatedOn: "12-06-2019",
    GroupLink: "https://t.me/Codewithrandom",
    image:
      "https://res.cloudinary.com/daafwyyne/image/upload/v1740634399/photo_2022-02-27_14-40-52_1_wn0c9w.gif",
  },
  {
    id: 2,
    name: "Parin",
    Channel: "Channel",
    members: 267,
    CreatedOn: "22-05-2016",
    GroupLink: "https://t.me/socialcashclubnetworks",
    image:
      "https://res.cloudinary.com/daafwyyne/image/upload/v1740633891/photo_2024-02-02_18-25-34_qu9pfe.gif",
  },
  {
    id: 3,
    name: "RealTalkExotics",
    Channel: "Channel",
    members: 842,
    CreatedOn: "15-08-2013",
    GroupLink: "https://t.me/joinchat/AAAAAEeia4j58ZoubNx8vw",
    image:
      "https://res.cloudinary.com/daafwyyne/image/upload/v1740634038/photo_2024-10-03_18-25-21_bd1ac1.jpg",
  },
  {
    id: 4,
    name: "Dmedical Forum",
    Channel: "Channel",
    members: 1248,
    CreatedOn: "12-12-2012",
    GroupLink: "https://t.me/never_have_i_ever_hindi",
    image:
      "https://res.cloudinary.com/daafwyyne/image/upload/v1740634132/photo_2024-06-26_01-24-32_e9fvlj.jpg",
  },
  {
    id: 5,
    name: "STREET DRUGS AVENUE 187",
    Channel: "Channel",
    members: 2234,
    CreatedOn: "10-10-2010",
    GroupLink: "https://t.me/+Uqr6WN1HanVjZGVi",
    image:
      "https://res.cloudinary.com/daafwyyne/image/upload/v1740634223/photo_2024-08-27_16-12-21_g0bkyd.jpg",
  },
];

const ProductsTable = () => {
  const [searchTerm, setSearchTerm] = useState("");
  const [filteredProducts, setFilteredProducts] = useState(PRODUCT_DATA);

  const handleSearch = (e) => {
    const term = e.target.value.toLowerCase();
    setSearchTerm(term);
    const filtered = PRODUCT_DATA.filter(
      (product) =>
        product.name.toLowerCase().includes(term) ||
        product.Channel.toLowerCase().includes(term)
    );

    setFilteredProducts(filtered);
  };

  return (
    <motion.div
      className="bg-[#1E1F26] shadow-lg rounded-xl p-6 border border-gray-700 mb-8"
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: 0.2 }}
    >
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-xl font-semibold text-gray-100">Groups List</h2>
        <div className="relative">
          <input
            type="text"
            placeholder="Search groups..."
            className="bg-gray-700 text-white placeholder-gray-400 rounded-lg pl-10 pr-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            onChange={handleSearch}
            value={searchTerm}
          />
          <Search className="absolute left-3 top-2.5 text-gray-400" size={18} />
        </div>
      </div>

      <div className="overflow-x-auto">
        <table className="min-w-full divide-y divide-gray-700">
          <thead>
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">
                Name
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">
                Channel/Chat
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">
                members
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">
                Created On
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">
                Group Link
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">
                Actions
              </th>
            </tr>
          </thead>

          <tbody className="divide-y divide-gray-700">
            {filteredProducts.map((product) => (
              <motion.tr
                key={product.id}
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ duration: 0.3 }}
              >
                <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-100 flex gap-2 items-center">
                  <img
                    src={product.image}
                    alt="Product img"
                    className="size-10 rounded-full"
                  />
                  {product.name}
                </td>

                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-300">
                  {product.Channel}
                </td>

                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-300">
                  {product.members}
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-300">
                  {product.CreatedOn}
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-300">
                  <a href={product.GroupLink} target="_blank">
                    Click Here
                  </a>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-300">
                  <button className="text-indigo-400 hover:text-indigo-300 mr-2">
                    <Edit size={18} />
                  </button>
                  <button className="text-red-400 hover:text-red-300">
                    <Trash2 size={18} />
                  </button>
                </td>
              </motion.tr>
            ))}
          </tbody>
        </table>
      </div>
    </motion.div>
  );
};
export default ProductsTable;
