from math import floor

from tqdm import tqdm
from PIL import Image

font = Image.open('4x6.png')

example_paper_text = """A Disproof By Counterexample of the Newman Integer Value Conjecture
Ezra Newman | 2022
Conjecture 1 from [1] is false because:
6 > 5

References
[1] Ezra Newman (2022). The Best Paper Ever Written, Sigbovik."""


def render_paper(paper_text: str) -> Image:
	lines = paper_text.split("\n")

	max_line_len = sorted([len(x) for x in lines])[-1]

	img = Image.new('RGB', (max_line_len * 4, 6 * len(lines)), "white")
	pixels = img.load()  # Create the pixel map

	def render_line(line_no: int, text: str):
		for i in range(len(text)):
			offset = ord(text[i])

			x_start = offset * 4
			x_end = x_start + 4

			crop_rect = (x_start, 0, x_end, 6)
			char = font.crop(crop_rect)
			img.paste(char, (i * 4, line_no * 6))

	for i in range(len(lines)):
		render_line(i, lines[i])

	return img


if __name__ == "__main__":
	example = render_paper(example_paper_text)
	page_size = (int(8.5 * 4800), 11 * 4800)
	# page_size = (example.size[0] * 10, example.size[1] * 10)

	n = 6
	page_count = -1
	while n < 600_010:
		page_count += 1
		page = Image.new('1', page_size, "white")
		x_paper_count: int = floor(page.size[0] / (example.size[0] + 4))
		y_paper_count: int = floor(page.size[1] / (example.size[1] + 4))
		print(x_paper_count, y_paper_count)
		for x in tqdm(range(x_paper_count)):
			for y in range(y_paper_count):
				cur_paper_text = f"""A Disproof By Counterexample of the Newman Integer Value Conjecture
Ezra Newman | 2022
Conjecture 1 from [1] is false because:
{n} > 5

References
[1] Ezra Newman (2022). The Best Paper Ever Written, Sigbovik."""
				n += 1
				paper = render_paper(cur_paper_text)
				page.paste(paper, ((example.size[0] + 4) * x, (example.size[1] + 4) * y))

		page.save(f'page{page_count}.png')
