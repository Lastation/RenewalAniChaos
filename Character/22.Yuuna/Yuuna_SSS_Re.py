import Function as f;

const s = StringBuffer();

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {                        
            f.NxNSquareShape(cp, 1, "40 + 1n Wraith", 3, 75);
            f.NxNSquareShape(cp, 1, " Unit. Hoffnung 25000", 3, 75);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {
            f.NxNSquareShape(cp, 1, "40 + 1n Wraith", 5, 75);
            f.NxNSquareShape(cp, 1, " Unit. Hoffnung 25000", 5, 75);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {
            f.NxNSquareShape(cp, 1, "50 + 1n Battlecruiser", 3, 75);
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {
            f.SquareShape(cp, 1, "Protoss Dark Archon", 150, 150);
            f.SquareShape(cp, 1, "Protoss Dark Archon", 150, 75);
            f.SquareShape(cp, 1, "Protoss Dark Archon", 150, 0);
            f.SquareShape(cp, 1, "Protoss Dark Archon", 150, -75);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 150, 150);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 150, 75);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 150, 0);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 150, -75);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 4)
         {         
            f.SquareShape(cp, 1, "Protoss Dark Archon", 150, 150 - 75 * f.loop[cp]);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 150, 150);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 150, 75);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 150, 0);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 150, -75);
            f.SquareShape(cp, 1, "50 + 1n Tank", 150, 150);
            f.SquareShape(cp, 1, "50 + 1n Tank", 150, 75);
            f.SquareShape(cp, 1, "50 + 1n Tank", 150, 0);
            f.SquareShape(cp, 1, "50 + 1n Tank", 150, -75);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }


      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] == 0)
         {
            f.SquareShape(cp, 1, "40 + 1n Mojo", 100, 100);
            f.SquareShape(cp, 1, "40 + 1n Mojo", 100, 50);
            f.SquareShape(cp, 1, "40 + 1n Mojo", 100, 0);
            f.SquareShape(cp, 1, "40 + 1n Mojo", 100, -50);
            f.SquareShape(cp, 1, "60 + 1n Archon", 100, 100);
            f.SquareShape(cp, 1, "60 + 1n Archon", 100, 50);
            f.SquareShape(cp, 1, "60 + 1n Archon", 100, 0);
            f.SquareShape(cp, 1, "60 + 1n Archon", 100, -50);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.NxNSquareShape(cp, 1, "40 + 1n Mojo", 3, 50);
            f.NxNSquareShape(cp, 1, "60 + 1n Archon", 3, 50);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 3)
      {
         KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

         f.SkillEnd(cp);
      }
   }
}