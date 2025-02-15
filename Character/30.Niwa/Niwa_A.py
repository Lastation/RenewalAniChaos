import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] < 8)
         {
            f.DotShape(cp, 1, "40 + 1n Gantrithor", 0, 0);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 8)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 4)
         {
            var x = 150;
            var y = 50 * f.loop[cp];

            for (var i = 0; i < 4; i++)
            {
               f.SquareShape(cp, 1, "40 + 1n Gantrithor", x - 50 * i, y);
            }
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
         }
         if (f.loop[cp] == 4)
         {
            f.SquareShape(cp, 1, "40 + 1n Mojo", 75, 75);
            f.SquareShape(cp, 1, "40 + 1n Mojo", 75, 150);
            f.SquareShape(cp, 1, "40 + 1n Mojo", 150, 75);
            f.SquareShape(cp, 1, "40 + 1n Mojo", 150, 150);

            f.SquareShape(cp, 1, "60 + 1n Dragoon", 75, 75);
            f.SquareShape(cp, 1, "60 + 1n Dragoon", 75, 150);
            f.SquareShape(cp, 1, "60 + 1n Dragoon", 150, 75);
            f.SquareShape(cp, 1, "60 + 1n Dragoon", 150, 150);

            f.SquareShape(cp, 1, "60 + 1n Danimoth", 0, 75);
            f.SquareShape(cp, 1, "60 + 1n Danimoth", 0, 150);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
            Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);
         }

         f.SkillWait(cp, 160);

         f.loop[cp] += 1;

         if (f.loop[cp] == 8)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] < 5)
         {
            KillUnitAt(4, "40 + 1n Mojo", "Anywhere", cp);

            if (f.loop[cp] == 2) KillUnitAt(4, "60 + 1n Danimoth", "Anywhere", cp);
            else
            {
               KillUnitAt(1, "60 + 1n Danimoth", "Anywhere", cp);
               KillUnitAt(4, "60 + 1n Dragoon", "Anywhere", cp);
            }
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 5)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 3)
      {

         f.SkillEnd(cp);
      }
   }
}