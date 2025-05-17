import { useEffect, useState } from "react";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

const ToastMessages = () => {
  const [index, setIndex] = useState(0);

  useEffect(() => {
    const messages = [
      "Suspicious message detected \n Tap to view",
      "Suspicious message detected \n Tap to view",
      "Suspicious message detected \n Tap to view",
    ];

    const showNextToast = () => {
      toast.error(messages[index], {
        onClose: () => {
          setTimeout(() => {
            setIndex((prevIndex) => (prevIndex + 1) % messages.length);
          }, 100000);
        },
      });
    };

    showNextToast();

    return () => {};
  }, [index]);

  return (
    <div>
      <ToastContainer
        position="bottom-center"
        autoClose={5000}
        theme="colored"
      />
    </div>
  );
};

export default ToastMessages;
