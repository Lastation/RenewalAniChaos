import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            f.EdgeShape(cp, 1, "40 + 1n Gantrithor", 45, 2, 75);
            f.EdgeShape(cp, 1, "60 + 1n Dragoon", 45, 2, 75);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
         }
         if (f.loop[cp] == 4)
         {
            f.EdgeShape(cp, 1, "40 + 1n Gantrithor", 45, 4, 150);
            f.EdgeShape(cp, 1, "60 + 1n Dragoon", 45, 4, 150);
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
         if (f.loop[cp] == 0)
         {
            f.SquareShape(cp, 1, "40 + 1n Mojo", 100, 0);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
         }
         if (f.loop[cp] == 2)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Mojo", 100, 100);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
         }
         if (f.loop[cp] == 4)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
         }
         if (f.loop[cp] == 6)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.SquareShape(cp, 1, "60 + 1n Danimoth", 50, 50);
            f.SquareShape(cp, 1, "60 + 1n Danimoth", 50, 0);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);
         }


         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 8)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", cp);

         f.SkillEnd(cp);
      }
   }
}