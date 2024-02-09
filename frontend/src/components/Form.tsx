import { Box, Button, TextInput } from "@mantine/core";
import { useForm } from "@mantine/form";

export function Form() {
  const form = useForm({
    initialValues: {
      knownTech: "",
      unknownTech: "",
      topics: "",
    },
  });

  return (
    <Box>
      <form onSubmit={form.onSubmit((values) => console.log(values))}>
        <TextInput label="Tech you know" {...form.getInputProps("knownTech")} />
        <TextInput label="Tech you don't know" {...form.getInputProps("unknownTech")} />
        <TextInput label="Topics you like" {...form.getInputProps("topics")} />
      <Button type="submit">Submit</Button>
      
      
      </form>
    </Box>
  );
}
