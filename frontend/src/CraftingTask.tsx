import { useCallback } from 'react';
import Box from '@material-ui/core/Box';
import Button from '@material-ui/core/Button';

interface ICraftingTaskProps
{
  color?: "inherit" | "primary" | "secondary" | "default";
}

function CraftingTask(props: ICraftingTaskProps) {
  const data = ["a", "b", "c"];

  const clickHandler = useCallback(() => {
    alert('clicked');
  }, []);

  return(
    <Box>
      <Button onClick={clickHandler} variant="contained" color={props.color}>
        This is a button
      </Button>
    </Box>
  );
}

export default CraftingTask;
