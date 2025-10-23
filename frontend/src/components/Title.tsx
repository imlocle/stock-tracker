import { motion } from 'framer-motion';
import '@styles/Title.css';

const Title = ({ title }: { title: string }) => {
  return (
    <motion.div
      className="title-header"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.8 }}
    >
      <motion.h1
        className="title"
        initial={{ y: -30, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ delay: 0.2, duration: 0.8 }}
      >
        {title}
      </motion.h1>
      <motion.div
        className="title-underline"
        initial={{ width: 0 }}
        animate={{ width: '80px' }}
        transition={{ delay: 0.5, duration: 0.8 }}
      />
    </motion.div>
  );
};

export default Title;
