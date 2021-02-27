import Box from '@material-ui/core/Box';
import Button from '@material-ui/core/Button';

interface ICraftingTaskProps
{
  color?: "inherit" | "primary" | "secondary" | "default";
}

function CraftingTask(props: ICraftingTaskProps) {
  return(
    <Box>
      <Button onClick={() => { alert('clicked') }} variant="contained" color={props.color}>
        Primary
      </Button>
    </Box>
  );
}

export default CraftingTask;
